
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from ..libs.liblinearutil import train
from ..datasets.data_manipulate import check_inputs, modify_y, check_y
from ..base import SaferEnsemble

__all__ = ['SafetyForecast']


class SafetyForecast(SaferEnsemble):
    """Provide a safer prediction when given a set of training models or 
    predict results. Judge the quality of prediction with large-margin model.

    Parameters
    ----------
    C1 : float (default=1.0)
        weight for the hinge loss of labeled instances. It was set as 1 in
        our paper.

    C2: float (default=0.01)
        weight for the hinge loss of unlabeled instances. It was set as
        0.01 in our paper.

    pred_values: predict values

    fallback_ind: fallback indexs of  unsafe prediction.

    estimators:list of estimators,optional (default=None)
        When 'estimators' is none, it means user should provide predictive 
        results. When 'estimators' is a list,each member of list is a tuple. 
        Each tuple is an initialization of a estimator and a description of its 
        parameters [(estimator,fit_params)].

    Examples
    --------
    When the 'estimators' parameter is initialized, the calling method is 
    roughly as follows:

    >>> from safeu.classification.TSVM import TSVM
    >>> from safeu.model_uncertainty.S4VM import S4VM
    >>> estimator_list = [(TSVM(),False), (S4VM(),True)]
    >>> model = SafetyForecast(estimators=estimator_list)
    >>> model.fit(x, y, l_ind)
    >>> model.predict(u_ind)
    
    It can be used like this when the 'estimators' is None: 
    
    >>> model = SafetyForecast()
    >>> model.fit(prediction, y, l_ind)
    >>> model.predict(u_ind, baseline_pred)

    """

    def __init__(self, C1=1.0, C2=0.01, estimators=None):

        self.C1 = C1
        self.C2 = C2
        self.estimators = estimators

        self.pred_values = None
        self.fallback_ind = None
        self.baseline_pred = None
        self.n_labels = None

    def set_params(self, param):
        """Parameter setting function.

        Parameters
        ----------
        param ：dict
            Store parameter names and corresponding values {'name': value}.
        """
        if isinstance(param, dict):
            self.__dict__.update(param)

        self.pred_values = None
        self.fallback_ind = None
        self.baseline_pred = None
        self.n_labels = None

    def fit(self, X, y, l_ind):
        """Provide an interface that can pass in multiple learners or 
        predictive results.

        Parameters
        ----------
        X : array-like
            Data matrix with [n_samples, n_features] or a set of prediction.

        y : array-like
            Each element is +1 or -1 for labeled instances. For unlabeled 
            instances, this parameter could be used for computing accuracy if 
            the ground truth is available.

        l_ind : array-like
            a row vector with length l, where l is the number of labeled
            instance. Each element is an index of a labeled instance.
        """
        N = X.shape[0]
        u_ind = np.linspace(0, N - 1, N).astype(np.int)
        u_ind = np.delete(u_ind, l_ind)

        if self.estimators is None:
            self.fit_pred(X, y, l_ind, u_ind)
        else:
            self.fit_estimators(X, y, l_ind, u_ind)

    def fit_estimators(self, X, y, l_ind, u_ind):
        """Provide a training interface that trains multiple models and give
        a safer prediction of these models.

        Parameters
        ----------
        X : array-like
            Data matrix with [n_samples, n_features].The data will be used to
            train models.

        y : array-like
            Each element is +1 or -1 for labeled instances. For unlabeled 
            instances, this parameter could be used for computing accuracy if 
            the ground truth is available.

        l_ind : array-like
            a row vector with length l, where l is the number of labeled
            instance. Each element is an index of a labeled instance.

        u_ind : array-like
            a row vector with length l, where l is the number of unlabeled
            instance. Each element is an index of a unlabeled instance.
        """
        predict_results = None

        for estimator, transductive in self.estimators:
            estimator.fit(X, y, l_ind)

            res_temp = np.zeros_like(y)
            res_temp[l_ind] = y[l_ind]
            if transductive:
                res_temp[u_ind] = estimator.predict(u_ind).reshape(-1, 1)
            else:
                res_temp[u_ind] = estimator.predict(X[u_ind]).reshape(-1, 1)

            if predict_results is None:
                predict_results = res_temp
            else:
                predict_results = np.hstack((predict_results, res_temp))

        self.fit_pred(predict_results, y, l_ind, u_ind)
        self._baseline_predict(X, y, l_ind, u_ind)

    def fit_pred(self, prediction, label, l_ind, u_ind):
        """Predict a safer result from predictions, train method judge the 
        quality of prediction with large-margin model

        Parameters
        ----------
        prediction : array-like
            A set of prediction.Each row is a set of predictive values of an 
            instance.Each col is a prediction result.

        label : array-like
            Each element is +1 or -1 for labeled instances. For unlabeled 
            instances, this parameter could be used for computing accuracy if 
            the ground truth is available.

        l_ind : array-like
            a row vector with length l, where l is the number of labeled
            instance. Each element is an index of a labeled instance.

        u_ind : array-like
            a row vector with length l, where l is the number of unlabeled
            instance. Each element is an index of a unlabeled instance.
        """
        param = '-q -s 3 -B 1'

        prediction_, label_, self.n_labels = check_inputs(prediction, label)

        y = np.zeros(np.size(label_))
        for i in l_ind:
            y[i] = label_[i]

        pos_ratio = np.sum(y[l_ind] == 1, 0) / np.size(l_ind)

        y[u_ind] = self._self_predict(
            np.sum(prediction_[u_ind, :], 1), pos_ratio)
        z = prediction_
        weight = np.zeros(np.size(y))
        weight[l_ind] = self._weight_balance(y[l_ind], self.C1)
        c2 = 1e-6

        while c2 < self.C2:
            weight[u_ind] = self._weight_balance(y[u_ind], c2)
            last_obj = float('inf')
            svm_model = train(weight.tolist(), y.tolist(), z.tolist(), param)
            w = np.hstack(svm_model.get_decfun())
            y[u_ind] = self._self_predict(
                np.dot(self._phi(z[u_ind, :]), np.transpose(w)), pos_ratio)
            obj = self._objective_value(
                np.transpose(w), self._phi(z), y, weight)
            while obj < last_obj:
                svm_model = train(weight.tolist(), y.tolist(),
                                  z.tolist(), param)
                y[u_ind] = self._self_predict(
                    np.dot(self._phi(z[u_ind, :]), np.transpose(w)), pos_ratio)
                last_obj = obj
                obj = self._objective_value(
                    np.transpose(w), self._phi(z), y, weight)
            c2 = c2 * 2

        self.w = np.hstack(svm_model.get_decfun())
        t1 = np.where(y * (np.dot(self._phi(z), np.transpose(w))) < 1)[0]

        self.fallback_ind = list(set(tuple(t1)).intersection(set(tuple(u_ind))))
        self.pred_values = y.reshape(-1, 1)

    def predict(self, u_ind, baseline_pred=None):
        """Predict method replace the unsafe prediction with the baseline_pred 
        to improve the safeness.

        Parameters
        ----------
        u_ind : array-like
            a row vector with length l, where l is the number of unlabeled
            instance. Each element is an index of a unlabeled instance.

        baseline_pred : array-like
            Each element is a baseline predictive result of the corresponding 
            instance. LEAD will replace the result of S3VM with this if the 
            instance locates in the margin of S3VM.

        Returns
        -------
        pred : a column vector with length n. Each element is a prediction for
            the label of the instance, including labeled and unlabeled
            instances, even though for labeled instances the prediction is
            consistent with the true label.
        """
        if baseline_pred is not None:
            self.baseline_pred = baseline_pred
        else:
            if self.baseline_pred is None:
                raise ValueError("Must provide baseline prediction matrix.")

        self.baseline_pred = self.baseline_pred.reshape(-1, 1)
        self.pred_values = modify_y(self.pred_values, range(
            0, len(self.pred_values)), self.n_labels)
        self.pred_values[self.fallback_ind] = \
                                        self.baseline_pred[self.fallback_ind]
        return self.pred_values[u_ind]

    def predict_proba(self):
        """Compute probabilities of possible labels for samples in W.

        Parameters
        ----------
        None

        Returns
        -------
        pred : array-like
            Each line is the probability of possible labels of a sample
            involved in the calculation of the prediction [n_samples, n_labels].
        """
        pass

    def _baseline_predict(self, X, y, l_ind, u_ind):
        """Use 1nn to provide baseline predictions, and when the 'estimators' 
        is not None, provide the own baseline for selection.

        Parameters
        ----------
        X : array-like
            Data matrix with [n_samples, n_features].The data will be used to
            train models.

        y : array-like
            Each element is +1 or -1 for labeled instances. For unlabeled 
            instances, this parameter could be used for computing accuracy if 
            the ground truth is available.

        l_ind : array-like
            A row vector with length l, where l is the number of labeled
            instance. Each element is an index of a labeled instance.

        u_ind : array-like
            a row vector with length l, where l is the number of unlabeled
            instance. Each element is an index of a unlabeled instance.
        """
        self.n_labels, label = check_y(y, binary=True)

        knn = KNeighborsClassifier()
        knn.fit(X[l_ind], label[l_ind].reshape(1, -1)[0].astype(int))
        baseline_pred = label
        baseline_pred[u_ind] = knn.predict(X[u_ind]).reshape(-1, 1)
        self.baseline_pred = modify_y(baseline_pred, np.linspace(
            0, len(baseline_pred) - 1, len(baseline_pred)).astype(np.int), 
            self.n_labels)

    def _accuracy(self, pred, target):
        """Compute accuracy for current prediction.

        Parameters
        ----------
        pred : array-like, shape = [n_samples]
            Labels of samples predicted by model.

        target : array-like, shape = [n_samples]
            True labels of samples.
        
        Returns
        -------
        acc : float
            Accuracy of predictions.
        """
        if np.size(pred) != np.size(target):
            raise ValueError(
                "The sizes of prediction and target are not matched.")
        return np.sum(pred == np.transpose(target)) / np.size(pred)

    def _phi(self, x):
        """
        """
        return np.hstack((x, np.ones((np.size(x, 0), 1))))

    def _weight_balance(self, y, C):
        """Compute weight of instances.

        Patameters
        ----------
        y : array-like, shape = [n_samples]
            Labels of samples.

        C : float
            Weight for the hinge loss of instances

        Returns
        -------
        weight : array-like, shape = [n_samples]
            weight of instances.
        """
        weight = np.ones(y.shape) * C
        weight[y == -1] = np.sum(y == 1) / np.sum(y == -1) * C
        return weight

    def _self_predict(self, f, r):
        """ Fix w and update the solution of y^ via Eq.(3) in paper [1].
        Corresponding to line 7 of Algo. 1

        Parameters
        ----------
        f : Predicting vector

        r : The ranks of the predictions on the unlabeled data.

        Return
        ------
        y : Updating y^
        """
        beta = 0
        u = np.size(f)
        y = np.sign(f)

        y[y == 0] = np.random.randint(1, 3, size=(np.sum(y == 0))) * 2 - 3
        rk = np.zeros((u, 1))
        ind = np.argsort(-f)

        for i in range(0, u):
            rk[ind[i]] = i

        for i in range(0, np.size(rk)):
            if (rk[i] - 1) / u <= r - beta:
                y[i] = 1
            elif (rk[i] - 1) / u <= r + beta:
                y[i] = -1

        assert (np.all(y != 0))

        return y

    def _objective_value(self, w, x, y, weight):
        """Compute value of objective function.

        Patameters
        ----------
        w : array-like
            Decision functions.

        x : array-like
            GSSL values.

        y : array-like
            Values of unlabeled instances.

        weight : array-like, shape = [n_samples]
            weight of instances.

        Returns
        -------
        obj : float
            Compute value of objective function.
        """
        t = 1 - y * (np.dot(x, w))
        t[t < 0] = 0
        return np.dot(np.transpose(w), w / 2) + np.dot(np.transpose(weight), t)
