# -*- coding: utf-8 -*-
"""
Class to implement the process of semi-supervised learning experiments.
"""
from .datasets import data_manipulate, base
from .base import BaseExperiments
from .utils.log_utils import get_logger
from sklearn.model_selection import ParameterGrid
from copy import deepcopy
from sklearn.externals.joblib import Parallel, delayed
import numpy as np

__all__ = ['SslExperimentsWithoutGraph', 'SslExperimentsWithGraph']

LOGGER = get_logger('Experiments')


class SslExperimentsWithoutGraph(BaseExperiments):
    """Semi-supervised learning experiments without graph.

    This class implements a common process of SSL experiments in both 
    transductive and inductive settings. It optimize the hyper-parameters 
    using grid-search policy which is paralleled using multi-processing. 

    Parameters
    ----------
    transductive : boolean, optional (default=True)
        The experiment is transductive if True else inductive.

    n_jobs : int, optional (default=1)
        The nunmber of jobs to run the experiemnt.

    all_class : boolean, optional (default=True)
        Whether all split should have all classes.
    
    Attributes
    ----------------
    performance_metric_name : string, optional (default='accuracy_score')
        The name of the metric.

    metri_param : dict, optional (default={})
        A dict store the 
    
    datasets : list
        A list of tuple which store the information of datasets to run.

    configs : list
        A list of tuple which store the information of algorithms to evaluate.

    performance_metric : callable
        A callable object which is the evaluating method.

    metri_param: dict
        A dict which store the parameters for self.performance_metric.

    Notes
    -----
    1. Multi-processing requests the estimator to be picklable. You may refer
       to `__getstate__` and `__setstate__` methods when your self-defined
       estimator has some problems with serialization.
    """

    def __init__(self, transductive=True, n_jobs=1,
                 metri_param=dict(), all_class=True):
        super(SslExperimentsWithoutGraph, self).__init__(
            transductive=transductive, n_jobs=n_jobs, all_class=all_class)

    def experiments_on_datasets(self, unlabel_ratio=0.8, test_ratio=0.3, 
                                number_init=5):
        """
        The datasets are splits randomly or based on given splits. Get 
        Label/Unlabel splits for each dataset in this funciton and conduct 
        experiments on them. Results are stored for each dataset.

        Parameters
        ----------
        unlabel_ratio : float
            The ratio of test data for each dataset.
        number_init : int
            Different label initializations for each dataset.
        
        Returns
        -------
        results : dict 
            {dataset_name: {config_name:[scores]} }
        """
        if len(self.datasets) == 0:
            LOGGER.debug("Haven't specified datasets.")
            return

        results = dict()  
        # dict: {dataset_name: {config_name:[scores]} }
        best_estimators = dict()
        # dict: {dataset_name: {config_name: [estimators]} }

        for name, feature_file, label_file, split_path, _ in self.datasets:
            # load dataset
            X, y = base.load_dataset(name, feature_file, label_file)
            LOGGER.debug("Load dataset {}".format(name))
            if split_path:  # provided split file
                _, test_idxs, labeled_idxs, unlabeled_idxs = \
                    data_manipulate.split_load(split_path, name)  
                # load split_file from disk
            else:  # no provided split file
                if self.transductive:
                    _, test_idxs, labeled_idxs, unlabeled_idxs = \
                        data_manipulate.inductive_split(X=X, y=y, 
                            test_ratio=0.,
                            initial_label_rate=1 - unlabel_ratio,
                            split_count=number_init,
                            all_class=self.all_class
                            )
                else:
                    _, test_idxs, labeled_idxs, unlabeled_idxs = \
                        data_manipulate.inductive_split(X=X, y=y, 
                            test_ratio=test_ratio, 
                            initial_label_rate=(
                                1 - test_ratio) * (1 - unlabel_ratio),
                            split_count=number_init,
                            all_class=self.all_class)
            
            results[name], best_estimators[name], preds = \
                self._experiment_on_single_dataset(X=X, y=y, 
                    labeled_idxs=labeled_idxs, unlabeled_idxs=unlabeled_idxs,
                    test_idxs=test_idxs, number_init=number_init)  # RUN

            self._evaluate_selected_model(data_name=name, preds=preds,
                                y_truth=y, unlabeled_idxs=unlabeled_idxs)
        #########
        # Do something on results
        #########
        LOGGER.info(results)
        return results

    def _experiment_on_single_dataset(self, X, y, labeled_idxs, unlabeled_idxs, 
                                        test_idxs, number_init=5):
        """
        Experiments with different label initialization on a single dataset.
        Called by experiments_on_datasets method.
        
        Parameters
        ----------
        X : np.ndarray
            Feaetures

        y : np.ndarray
            Labels

        labeled_idxs : list of [array-like]
            List of labeled_idxs

        unlabeled_idxs : list of [array-like]
            List of unlabeled_idxs
        
        test_idxs : list of [array-like]
            List of testing_idxs
        
        number_init : int
            Number of differnt initialized labeled data

        Returns
        -------
        AveScores : dict === {config_name : [float] }
            A dict storing the average result of each estimator

        BestEstimators : dict === {config_name : [estimator] }
            A dict storing the best estimator in each config
        
        preds: dict === {config_name : [np.ndarray] }
            A dict storing the prediction of the best estimator on testing data
        """
        # label/unlabel initialization
        number_init = len(labeled_idxs) if labeled_idxs is not None \
                                        else number_init  

        # experiments on given configs 

        scores = dict()  
        # config_name -> [score_1, score_2,..., score_num_initial]
        estimators = dict()  
        # config_name  -> [estimator_1, ..., estimator]
        preds = dict()

        for name, estimator, param_dict in self.configs:  # for all configs
            LOGGER.debug("Estimator: {}".format(name))
            if self.transductive:
                if self.n_jobs == 1 or self.n_jobs == 0:
                    scores[name] = [0.] * number_init
                    estimators[name] = [[]] * number_init 
                    preds[name] = [[]] * number_init
                    for i in range(number_init):  # for each data split
                        scores[name][i], estimators[name][i], preds[name][i] = \
                        SslExperimentsWithoutGraph._evaluate_on_single_split(
                            name=name, estimator=estimator, 
                            param_dict=param_dict, X=X, y=y, 
                            labeled_idx=labeled_idxs[i],
                            unlabeled_idx=unlabeled_idxs[i], 
                            performance_metric=self.performance_metric,
                            metri_param=self.metri_param,
                            metri_large_better=self.metri_large_better,
                            transductive=self.transductive)
                        
                else:  # Multiprocessing 
                    tmp = Parallel(n_jobs=min(number_init, self.n_jobs), 
                    verbose=30)(delayed(
                        SslExperimentsWithoutGraph._evaluate_on_single_split)(
                            name=name, estimator=deepcopy(estimator), 
                            param_dict=param_dict, X=X, y=y, 
                            labeled_idx=labeled_idxs[i],
                            unlabeled_idx=unlabeled_idxs[i], 
                            performance_metric=self.performance_metric,
                            metri_param=self.metri_param,
                            metri_large_better=self.metri_large_better,
                            transductive=self.transductive) 
                            for i in range(number_init))
                    scores[name] = [t[0] for t in tmp]
                    estimators[name] = [t[1] for t in tmp]
                    preds[name] = [t[2] for t in tmp]
                    
            else:
                if self.n_jobs == 1 or self.n_jobs == 0:
                    scores[name] = [0.] * number_init
                    estimators[name] = [[]] * number_init 
                    preds[name] = [[]] * number_init
                    for i in range(number_init):  # for each data split
                        scores[name][i], estimators[name][i], preds[name][i] = \
                        SslExperimentsWithoutGraph._evaluate_on_single_split(
                            name=name, estimator=estimator, 
                            param_dict=param_dict, X=X, y=y, 
                            labeled_idx=labeled_idxs[i],
                            unlabeled_idx=unlabeled_idxs[i], 
                            performance_metric=self.performance_metric,
                            metri_param=self.metri_param,
                            metri_large_better=self.metri_large_better,
                            transductive=self.transductive,
                            test_idx=test_idxs[i])
                        
                else:  # Multiprocessing 
                    tmp = Parallel(n_jobs=min(number_init, self.n_jobs), 
                        verbose=30)(delayed(
                        SslExperimentsWithoutGraph._evaluate_on_single_split)(
                            name=name, estimator=deepcopy(estimator), 
                            param_dict=param_dict, X=X, y=y, 
                            labeled_idx=labeled_idxs[i],
                            unlabeled_idx=unlabeled_idxs[i], 
                            performance_metric=self.performance_metric,
                            metri_param=self.metri_param,
                            metri_large_better=self.metri_large_better,
                            transductive=self.transductive,
                            test_idx=test_idxs[i])
                            for i in range(number_init))
                    scores[name] = [t[0] for t in tmp]
                    estimators[name] = [t[1] for t in tmp]
                    preds[name] = [t[2] for t in tmp]
        return scores, estimators, preds
    
    @classmethod
    def _evaluate_on_single_split(cls, name, estimator, param_dict, X, y, 
                                labeled_idx, unlabeled_idx, performance_metric, 
                                metri_param, metri_large_better, transductive,
                                test_idx=None, k=3, 
                                search_strategy="grid_search"):
        """
        Run single algorithm given parameters for a label initialization on 
        single dataset and get the evaluation in given metric.

        Implement the gridsearch hyper-param optimization.
        A unit of multiprocessing job.

        Parameters
        ----------
        name : string
        
        estimator : object
        X : np.ndarray

        y : np.ndarray
        
        labeled_idx ：np.ndarray
        
        unlabeled_idx : np.ndarray
        
        performance_metric : callable
        
        metri_param : dict

        metri_large_better : boolean
        
        transductive : boolean

        test_idx : np.ndarray or None, optional
            Used in inductive setting. Should be None when 
            self.transductive=True.
        k : int
            k-fold
        
        search_strategy : str

        Returns
        -------
        score: float
            Evaluation score on the test data.
        
        estimator: object
            The best model for the label initialization.
        
        pred: np.ndarray
            The prediction made by the best model.
        """

        param_list = list(ParameterGrid(param_dict))
        best_param = None
        best_score = -9999

        # label data split
        train_idxs, validation_idxs = data_manipulate.cv_split(X=X, y=y, 
                                instance_indexes=labeled_idx, k=k,
                                split_count=1, all_class=True)
        
        if transductive:  # transductive setting  
            for param in param_list: 
                # hyper-parameter optimization with CV or other methods.
                LOGGER.debug("Estimator: {}  params: {}".format(name, param))
                estimator.set_params(param)   # need set_params
                score = [0.] * len(train_idxs)
                # PARALLEL HERE 
                for i in range(len(train_idxs)):
                    estimator.fit(X, y, train_idxs[i])
                    pred = estimator.predict(validation_idxs[i])  

                    score[i] = performance_metric(y[validation_idxs[i]], pred,
                                                                metri_param)  
                    LOGGER.debug("Training performance {}/{}-Fold: {}".format(i,
                                                                k, score[i]))
                if metri_large_better:
                    if np.average(score) > best_score:
                        best_param = param
                        best_score = np.average(score)
                else:
                    if np.average(score) < best_score:
                        best_param = param
                        best_score = np.average(score)
            
            # Select the best_param, refit the estimator
            estimator.set_params(best_param)
            estimator.fit(X, y, labeled_idx)
            pred = estimator.predict(unlabeled_idx)
            best_score = performance_metric(y[unlabeled_idx], pred, metri_param)
            LOGGER.debug("Validation performance: {}".format(best_score))
            return best_score, estimator, pred
                    
        else:  # inductive setting  

            for param in param_list: 
                # hyper-parameter optimization with CV or other methods.
                LOGGER.debug("Estimator: {}  params: {}".format(name, param))
                estimator.set_params(param)   # need set_params
                score = [0.] * len(train_idxs)

                for i in range(len(train_idxs)):
                    # train with instances in train_idx and unlabeled_idx
                    idx_tmp = np.concatenate([train_idxs[i], unlabeled_idx])
                    X_tmp = X[idx_tmp, :]
                    y_tmp = y[idx_tmp, :]
                    estimator.fit(X_tmp, y_tmp, np.arange(len(train_idxs[i])))
                    pred = estimator.predict(X[validation_idxs[i], :])  

                    score[i] = performance_metric(y[validation_idxs[i]],
                                                pred, metri_param) 
                    LOGGER.debug("Training performance {}/{}-Fold: {}".format(i,
                                k, score[i]))
                if metri_large_better:
                    if np.average(score) > best_score:
                        best_param = param
                        best_score = np.average(score)
                else:
                    if np.average(score) < best_score:
                        best_param = param
                        best_score = np.average(score)
        
            # Select the best_param, refit the estimator
            estimator.set_params(best_param)
            # train with instances in labeled_idx and unlabeled_idx
            idx_tmp = np.concatenate([labeled_idx, unlabeled_idx])
            X_tmp = X[idx_tmp, :]
            y_tmp = y[idx_tmp, :]
            estimator.fit(X_tmp, y_tmp, np.arange(len(labeled_idx)))
            
            pred = estimator.predict(X[test_idx, :])
            best_score = performance_metric(y[test_idx], pred, metri_param) 

            return best_score, estimator, pred


class SslExperimentsWithGraph(BaseExperiments):
    """Semi-supervised learning experiments with graph.

    This class implements a common process of SSL experiments in both 
    transductive and inductive settings for graph-based methods. It optimize 
    the hyper-parameters using grid-search policy which is paralleled using 
    multi-processing. 

    Parameters
    ----------
    transductive : boolean, optional (default=True)
        The experiment is transductive if True else inductive.

    n_jobs : int, optional (default=1)
        The nunmber of jobs to run the experiemnt.

    all_class : boolean, optional (default=True)
        Whether all split should have all classes.
    
    Attributes
    ----------------
    performance_metric_name : string, optional (default='accuracy_score')
        The name of the metric.

    metri_param : dict, optional (default={})
        A dict store the 
    
    datasets : list
        A list of tuple which store the information of datasets to run.

    configs : list
        A list of tuple which store the information of algorithms to evaluate.

    performance_metric : callable
        A callable object which is the evaluating method.

    metri_param: dict
        A dict which store the parameters for self.performance_metric.

    Notes
    -----
    1. Multi-processing requests the estimator to be picklable. You may refer 
       to `__getstate__` and `__setstate__` methods when your self-defined 
       estimator has some problems with serialization.
    """

    def __init__(self, n_jobs=1):
        super(SslExperimentsWithGraph, self).__init__(
            transductive=True, n_jobs=n_jobs)

    def experiments_on_datasets(self, unlabel_ratio=0.8, test_ratio=0.3, 
                                number_init=5):
        """
        The datasets are splits randomly or based on given splits. Get 
        Label/Unlabel splits for each dataset in this funciton and conduct 
        experiments on them. Results are stored for each dataset.

        Parameters
        ----------
        unlabel_ratio : float
            The ratio of unlabeled data for each dataset.
        test_ratio : float
            The ratio of test data for each dataset. Is invalid when 
            `transductive` =True.
        number_init : int
            Different label initializations for each dataset.
        
        Returns
        -------
        results : dict 
            {dataset_name: {config_name:[scores]} }
        """
        if len(self.datasets) == 0:
            LOGGER.debug("Haven't specified datasets.")
            return

        results = dict()  
        # dict === {dataset_name: {config_name:[scores]} }
        best_estimators = dict()  
        # dict === {dataset_name: {config_name: [estimators]} }

        for name, feature_file, label_file, split_path, graph_file \
                                                            in self.datasets:
            # load dataset
            X, y = base.load_dataset(name, feature_file, label_file)
            W = base.load_graph(name, graph_file)

            if split_path:  # provided split file
                _, test_idxs, labeled_idxs, unlabeled_idxs = \
                    data_manipulate.split_load(split_path, name)  
                # load split_file from disk
            else:  # no provided split file
                if self.transductive:
                    _, test_idxs, labeled_idxs, unlabeled_idxs = \
                        data_manipulate.inductive_split(X=X, y=y, test_ratio=0.,
                        initial_label_rate=1 - unlabel_ratio, 
                        split_count=number_init, all_class=True, 
                        saving_path='.')
                else:
                    _, test_idxs, labeled_idxs, unlabeled_idxs = \
                        data_manipulate.inductive_split(X=X, y=y, 
                        test_ratio=test_ratio, 
                        initial_label_rate=(1 - test_ratio
                                            ) * (1 - unlabel_ratio),
                        split_count=number_init, all_class=True, 
                        saving_path='.')
            results[name], best_estimators[name], preds = \
                self._experiment_on_single_dataset(X=X, y=y, W=W, 
                labeled_idxs=labeled_idxs, unlabeled_idxs=unlabeled_idxs, 
                test_idxs=test_idxs, number_init=number_init)
            
            self._evaluate_selected_model(data_name=name, preds=preds,
                                y_truth=y, unlabeled_idxs=unlabeled_idxs)
        
        #########
        # Do something on results
        #########
        LOGGER.info(results)
        return results

    def _experiment_on_single_dataset(self, X, y, W, labeled_idxs, 
                                    unlabeled_idxs, test_idxs, number_init=5):
        """Experiments with different label initialization on a single dataset.
        
        Parameters
        ----------
        X : np.ndarray
            Feaetures

        y : np.ndarray
            Labels

        labeled_idxs : list of [array-like]
            List of labeled_idxs

        unlabeled_idxs : list of [array-like]
            List of unlabeled_idxs
        
        test_idxs : list of [array-like]
            List of testing_idxs
        
        number_init : int
            Number of differnt initialized labeled data

        Returns
        -------
        AveScores : dict === {config_name : [float] }
            A dict storing the average result of each estimator

        BestEstimators : dict === {config_name : [estimator] }
            A dict storing the best estimator in each config
        
        preds: dict === {config_name : [np.ndarray] }
            A dict storing the prediction of the best estimator on testing data
        """
        # label/unlabel initialization
        if not isinstance(labeled_idxs, list):
            labeled_idxs = labeled_idxs.tolist()

        number_init = len(labeled_idxs) if labeled_idxs else number_init  

        # experiments on given configs 

        scores = dict()
        # config_name -> [score_1, score_2,..., score_num_initial]
        estimators = dict()
        # config_name  -> [estimator_1, ..., estimator]
        preds = dict()

        for name, estimator, param_dict in self.configs:  # for all configs
            if self.n_jobs == 1 or self.n_jobs == 0:
                scores[name] = [0.] * number_init
                estimators[name] = [[]] * number_init 
                preds[name] = [[]] * number_init
                for i in range(number_init):  # for each data split
                    scores[name][i], estimators[name][i], preds[name][i] = \
                        SslExperimentsWithGraph._evaluate_on_single_split(
                        name=name, estimator=estimator, 
                        param_dict=param_dict, X=X, y=y, W=W,
                        labeled_idx=labeled_idxs[i],
                        unlabeled_idx=unlabeled_idxs[i], 
                        performance_metric=self.performance_metric,
                        metri_param=self.metri_param,
                        metri_large_better=self.metri_large_better,
                        transductive=self.transductive)
                    
            else:  # Multiprocessing 
                tmp = Parallel(n_jobs=min(number_init, self.n_jobs), 
                    verbose=30)(delayed(
                    SslExperimentsWithGraph._evaluate_on_single_split)(
                        name=name, estimator=estimator, 
                        param_dict=param_dict, X=X, y=y, W=W,
                        labeled_idx=labeled_idxs[i],
                        unlabeled_idx=unlabeled_idxs[i], 
                        performance_metric=self.performance_metric,
                        metri_param=self.metri_param,
                        metri_large_better=self.metri_large_better,
                        transductive=self.transductive)
                        for i in range(number_init))
                scores[name] = [t[0] for t in tmp]
                estimators[name] = [t[1] for t in tmp]
                preds[name] = [t[2] for t in tmp]
        return scores, estimators, preds
    
    @classmethod
    def _evaluate_on_single_split(cls, name, estimator, param_dict, X, y, W, 
                            labeled_idx, unlabeled_idx, performance_metric, 
                            metri_param, metri_large_better, transductive,
                            test_idx=None, k=3, search_strategy="grid_search"):
        """
        Run single algorithm given parameters for a label initialization on 
        single dataset and get the evaluation in given metric.

        Implement the gridsearch hyper-param optimization.
        A unit of multiprocessing job.

        Parameters
        ----------
        name : string
        
        estimator : object

        X : np.ndarray

        y : np.ndarray
        
        W : np.ndarray
        
        labeled_idx ：np.ndarray
        
        unlabeled_idx : np.ndarray
        
        performance_metric : callable
        
        metri_param : dict

        metri_large_better : boolean
        
        transductive : boolean

        test_idx : np.ndarray or None, optional
            Used in inductive setting. Should be None when 
            self.transductive=True.
        k : int
            k-fold
        
        search_strategy : str

        Returns
        -------
        score: float
            Evaluation score on the test data.
        
        estimator: object
            The best model for the label initialization.
        
        pred: np.ndarray
            The prediction made by the best model.
        
        Examples
        -------
        >>> param_grid = {'a': [1, 2], 'b': [True, False]}
        >>> list(ParameterGrid(param_grid)) == (
            [{'a': 1, 'b': True}, {'a': 1, 'b': False},
            {'a': 2, 'b': True}, {'a': 2, 'b': False}])
        >>> param_grid = {}
        >>> list(ParameterGrid(param_grid)) == [{}]
        """
        param_list = list(ParameterGrid(param_dict))
        best_param = None
        best_score = -9999

        # label data split
        train_idxs, validation_idxs = data_manipulate.cv_split(X=X, y=y, 
                                instance_indexes=labeled_idx, 
                                k=k, split_count=1, all_class=True)
        
        for param in param_list:
            # hyper-parameter optimization with CV or other methods.
            estimator.set_params(param)   # need set_params
            score = [0.] * len(train_idxs)
            for i in range(len(train_idxs)):
                estimator.fit(X, y, train_idxs[i], W)
                pred = estimator.predict(validation_idxs[i])  

                score[i] = performance_metric(y[validation_idxs[i]], pred, 
                                            metri_param)  
            
            if metri_large_better:
                if np.average(score) > best_score:
                    best_param = param
                    best_score = np.average(score)
            else:
                if np.average(score) < best_score:
                    best_param = param
                    best_score = np.average(score)
        
        # Select the best_param, refit the estimator
        estimator.set_params(best_param)
        estimator.fit(X, y, labeled_idx, W)
        pred = estimator.predict(unlabeled_idx)
        best_score = performance_metric(y[unlabeled_idx], pred, metri_param) 
        return best_score, estimator, pred
