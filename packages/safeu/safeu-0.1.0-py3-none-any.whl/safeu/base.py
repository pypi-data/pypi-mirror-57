"""Base classes for all estimators and experiments."""

import re

import numpy as np

from abc import abstractmethod, ABC
from .utils.log_utils import get_logger
from .metrics import performance

LOGGER = get_logger("safeu.base")

########################
# BaseExperiments
########################


class BaseExperiments(object):
    '''
    The base class for all experiments.
    You can inherit this class to design you own experiment process.

    '''
    def __init__(self, transductive=True, n_jobs=1, all_class=True):
        self.datasets = []
        self.splits = []
        self.configs = []
        self.evaluate_metric_name = []
        self.evaluate_metric = []
        self.evaluate_metri_param = []
        self.evaluate_results = dict()
        # evaluate_result[data_name][config_name][evaluate_name] -> [0.]
        self.performance_metric = getattr(performance, "accuracy_score")  
        self.metri_param = {}
        self.metri_large_better = True
        self.transductive = transductive
        self.n_jobs = n_jobs
        self.all_class = all_class
        pass

    def append_configs(self, configs):
        """Append estimators configs to self.config

        Parameters
        ----------
        configs: list of (name, estimator, param_dict)
            In which name: string, estimator: object of estimator, 
            param_dict: dict of parameters for corresponding estimator.
        """
        for name, estimator, param_dict in configs:
            self._append_config(name, estimator, param_dict)

    def _append_config(self, name, estimator, param_dict):
        """Append estimator config to self.config
        self.config is list of tuple (string, estimator, param_dict)
        
        Parameters
        ----------
        name: string
        estimator： object of estimator
        param_dict:  dict of parameters for estimators
        """
        self.configs.append((name, estimator, param_dict))
    
    def append_datasets(self, datasets):
        """Append datasets file names to self.datasets
        
        Parameters
        ----------
        datasets: list of (name,feature_file,label_file,split_path,graph_file)
            Detais::

            name: string
                Name of the dataset. Arbitrary
            feature_file: string or None
                Absolute file name of the feature file. Can be any thing if 
            label_file: string or None
                Absolute file name of the label file.
            split_path: string or None
                Absolute path in which store the split files. Should be None if 
                no split files is provided.
            graph_file: string or None
                Absolute file name of the graph files. Should be None if no 
                graph is provided.
        """
        for name, feature_file, label_file, split_path, graph_file in datasets:
            self._append_dataset(name, feature_file, label_file, split_path,
                                graph_file)

    def _append_dataset(self, name, feature_file, label_file, split_path,
                        graph_file):
        """Append dataset file name to self.datasets
        
        self.datasets is list of tuple (string, string, string)
        
        Parameters
        ----------
        name: string
            Name of the dataset
        feature_file: string
            Absolute file name of the feature file.
        label_file: string
            Absolute file name of the label file. 
        split_path: string 
            Absolute path in which store the split files. Should be None if no 
            split files is provided.
        graph_file: string
            Absolute file name of the graph files. Should be None if no 
            graph is provided.
        """
        self.datasets.append(
            (name, feature_file, label_file, split_path, graph_file)
            )

    def set_metric(self, performance_metric='accuracy_score', 
                metric_large_better=True, param_dict=None):
        """
        Set the metric for experiment.

        Parameters
        ------------
        performace_metric: str 
            The query performance-metric function.
            Giving str to use a pre-defined performance-metric.
            
        kwargs: dict, optional
            The args used in performance-metric.
            if kwargs is None,the pre-defined performance will init in the 
            default way. Note that, each parameters should be static.      
        """
        if performance_metric not in [
                                    'accuracy_score',
                                    'zero_one_loss',
                                    'roc_auc_score',
                                    'get_fps_tps_thresholds',
                                    'hamming_loss',
                                    'one_error',
                                    'f1_score',
                                    'coverage_error',
                                    'label_ranking_loss',
                                    'label_ranking_average_precision_score',
                                    'micro_auc_score',
                                    'average_precision_score',
                                    'minus_mean_square_error']:
            raise NotImplementedError('Performance {} is not'
                ' implemented.'.format(str(performance_metric)))
        # Need to modify
        if param_dict is None:
            param_dict = {}
        self.performance_metric_name = performance_metric
        self.performance_metric = getattr(performance, performance_metric)
        self.metri_param = param_dict
        self.metri_large_better = metric_large_better
    
    def append_evaluate_metric(self, performance_metric='accuracy_score',
                                kwargs=dict()):
        """
        Append the metric for evaluation.

        Parameters
        ------------
        performace_metric: str 
            The query performance-metric function.
            Giving str to use a pre-defined performance-metric.
            
        kwargs: dict, optional
            The args used in performance-metric.
            if kwargs is None,the pre-defined performance will init in the 
            default way. Note that, each parameters should be static.
                
        """
        if performance_metric not in [
                                    'accuracy_score',
                                    'zero_one_loss',
                                    'roc_auc_score',
                                    'get_fps_tps_thresholds',
                                    'hamming_loss',
                                    'one_error',
                                    'f1_score',
                                    'coverage_error',
                                    'label_ranking_loss',
                                    'label_ranking_average_precision_score',
                                    'micro_auc_score',
                                    'average_precision_score',
                                    'minus_mean_square_error']:
            raise NotImplementedError('Performance {} is not'
                ' implemented.'.format(str(performance_metric)))
        # Need to modify

        self.evaluate_metric_name.append(performance_metric)
        self.evaluate_metric.append(getattr(performance, performance_metric))
        self.evaluate_metri_param.append(kwargs)
    
    def _evaluate_selected_model(self, data_name, preds, y_truth,
                                unlabeled_idxs):
        """
        Evaluate the predictions with some metrics configured for this
        experiments in `evaluate_metric`.
        """
        if len(self.evaluate_metric_name) == 0:
            return
        assert len(self.configs) > 0
        assert len(preds[self.configs[0][0]]) == len(unlabeled_idxs)

        self.evaluate_results[data_name] = dict()
        
        for config_name, _, _ in self.configs:
            self.evaluate_results[data_name][config_name] = dict()
            for name, metric, param in zip(self.evaluate_metric_name,
                    self.evaluate_metric, self.evaluate_metri_param):
                self.evaluate_results[data_name][config_name][name] = []
                for i in range(len(preds[config_name])):
                    self.evaluate_results[data_name][config_name][name].append(
                        metric(y_truth[unlabeled_idxs[i]], 
                                preds[config_name][i], param)
                    )

    def get_evaluation_results(self):
        return self.evaluate_results


#########################
# BaseEstimator
#########################
def _pprint(params, offset=0, printer=repr):
    """Pretty print the dictionary 'params'.
    
    Parameters
    ----------
    params : dict
        The dictionary to pretty print

    offset : int
        The offset in characters to add at the begin of each line.

    printer : callable
        The function to convert entries to strings, typically
        the builtin str or repr
    """
    # Do a multi-line justified repr:
    options = np.get_printoptions()
    np.set_printoptions(precision=5, threshold=64, edgeitems=2)
    params_list = list()
    this_line_length = offset
    line_sep = ',\n' + (1 + offset // 2) * ' '
    # for i, (k, v) in enumerate(sorted(six.iteritems(params))):
    for i, (k, v) in enumerate(params.items()):
        if type(v) is float:
            # use str for representing floating point numbers
            # this way we get consistent representation across
            # architectures and versions.
            this_repr = '%s=%s' % (k, str(v))
        else:
            # use repr of the rest
            this_repr = '%s=%s' % (k, printer(v))
        if len(this_repr) > 500:
            this_repr = this_repr[:300] + '...' + this_repr[-100:]
        if i > 0:
            if (this_line_length + len(this_repr) >= 75 or '\n' in this_repr):
                params_list.append(line_sep)
                this_line_length = len(line_sep)
            else:
                params_list.append(', ')
                this_line_length += 2
        params_list.append(this_repr)
        this_line_length += len(this_repr)

    np.set_printoptions(**options)
    lines = ''.join(params_list)
    # Strip trailing space to avoid nightmare in doctests
    lines = '\n'.join(l.rstrip(' ') for l in lines.split('\n'))
    return lines


class BaseEstimator(ABC):
    """
    Base class for all estimators in safeu.
    Notes
    -----
    All estimators should specify all the parameters that can be set
    at the class level in their ``__init__`` as explicit keyword
    arguments (no ``*args`` or ``**kwargs``).
    """

    def __init__(self):
        pass

    @abstractmethod
    def set_params(self, param):
        """
        Update the parameters of the estimator and release old results to 
        prepare for new training.
        """
        raise NotImplementedError()
    
    def _get_attr_names(self) -> []:
        """Get attributes of the class.
        
        Return
        ------
        Sorted list of attribute names.
        """
        return sorted([a for a, v in self.__dict__.items()
                if not re.match('<function.*?>', str(v)) and not
                (a.startswith('__') and a.endswith('__'))])

    def get_params(self, deep=True):
        """Get parameters for this estimator.
        
        Parameters
        ----------
        deep : boolean, optional
            If True, will return the parameters for this estimator and
            contained subobjects that are estimators.
        
        Returns
        -------
        params : mapping of string to any
            Parameter names mapped to their values.
        """
        out = dict()
        for key in self._get_attr_names():
            value = getattr(self, key, None)
            if deep and hasattr(value, 'get_params'):  
                # get parameters of contained subobjects
                deep_items = value.get_params().items()
                out.update((key + '__' + k, val) for k, val in deep_items)
            out[key] = value
        return out

    def __repr__(self):
        """ 
        Need Test.
        """
        class_name = self.__class__.__name__
        return '%s(%s)' % (class_name, _pprint(self.get_params(deep=False),
                                               offset=len(class_name),),)


class TransductiveEstimatorwithGraph(BaseEstimator):

    @abstractmethod
    def __init__(self):
        super(TransductiveEstimatorwithGraph, self).__init__()

    @abstractmethod
    def fit(self, X, y, l_ind, W, **kwargs):
        """Takes X, y, label_index, affinity matrix"""
        raise NotImplementedError()
    
    @abstractmethod
    def predict(self, u_ind, **kwargs):
        """Takes unlabel_index"""
        raise NotImplementedError()


class TransductiveEstimatorWOGraph(BaseEstimator):

    @abstractmethod
    def __init__(self):
        super(TransductiveEstimatorWOGraph, self).__init__()

    @abstractmethod
    def fit(self, X, y, l_ind, **kwargs):
        """Takes X, y, label_index"""
        raise NotImplementedError()
    
    @abstractmethod
    def predict(self, u_ind, **kwargs):
        """Takes unlabel_index"""
        raise NotImplementedError()


class InductiveEstimatorWOGraph(BaseEstimator):

    @abstractmethod
    def __init__(self):
        super(InductiveEstimatorWOGraph, self).__init__()

    @abstractmethod
    def fit(self, X, y, l_ind, **kwargs):
        """Takes X, y, label_index"""
        raise NotImplementedError()
    
    @abstractmethod
    def predict(self, X, **kwargs):
        """Takes X"""
        raise NotImplementedError()


class InductiveEstimatorwithGraph(BaseEstimator):

    @abstractmethod
    def __init__(self):
        super(InductiveEstimatorwithGraph, self).__init__()

    @abstractmethod
    def fit(self, X, y, l_ind, W, **kwargs):
        """Takes X, y, label_index, affinity matrix"""
        raise NotImplementedError()
    
    @abstractmethod
    def predict(self, X, **kwargs):
        """Takes X"""
        raise NotImplementedError()


class SupervisedEstimator(BaseEstimator):
    """ Supervised estimator of single-label task.
    """

    @abstractmethod
    def __init__(self):
        super(SupervisedEstimator, self).__init__()
        self.model = None

    def fit(self, X, y, l_ind=None, **kwargs):
        """
        Takes X, y, label_index.
        """
        if l_ind is not None:
            X = X[l_ind, :]
            if y.ndim == 2:
                y = y[l_ind, :].reshape(-1)
            else:
                y = y[l_ind]
        self.model.fit(X, y)
    
    def predict(self, X, **kwargs):
        """
        Takes X
        """
        return self.model.predict(X)
    
    def set_params(self, param):
        self.model.set_params(**param)
    
    def predict_proba(self, X):
        return self.model.predict_proba(X)
    
    def predict_log_proba(self, X):
        return self.model.predict_log_proba(X)
    

#########################
# BaseEnsemble
#########################

class SaferEnsemble(BaseEstimator):
    '''
    Base class for SaferEnsemble for semi-supervised learning.
    Notes
    -----
    All estimators should specify all the parameters that can be set
    at the class level in their ``__init__`` as explicit keyword
    arguments (no ``*args`` or ``**kwargs``).
    '''
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def fit(self, X, y, l_ind, **kwargs):
        """Fit the model with base semi-supervised predictions.
        """
        raise NotImplementedError()
    
    @abstractmethod
    def predict(self, u_ind, baseline_pred=None):
        """
        Should provide baseline prediction. Can only make safer prediction
        with given ones, so it's transductive. 
        """
        raise NotImplementedError()
    

#########################
# Basemetric
#########################
