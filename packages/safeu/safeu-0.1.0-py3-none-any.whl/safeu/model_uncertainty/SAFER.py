"""
SAFER implements the SAFER algorithm in [1].
========================================================================

References
----------
..  [1] Yu-Feng Li, Han-Wen Zha and Zhi-Hua Zhou. Construct Safe Prediction 
    from Multiple Regressors. In: The 31st AAAI Conference on Artificial 
    Intelligence % (AAAI'17), San Francisco, California, 2017.
"""
from sklearn.neighbors import KNeighborsClassifier
from cvxopt import solvers, matrix
import numpy as np
from ..base import InductiveEstimatorWOGraph


class SAFER(InductiveEstimatorWOGraph):

    def __init__(self, estimator=False):
        super(SAFER, self).__init__()
        self.baseline_prediction = None
        self.Safer_prediction = 0.0
        self.estimator = estimator
        self.prediction = None

    def set_params(self, param):
        """Parameter setting function.

        Parameters
        ----------
        param ：dict
            Store parameter names and corresponding values {'name': value}.
        """
        self.baseline_prediction = None
        self.Safer_prediction = 0.0
        if isinstance(param, dict):
            self.__dict__.update(param)

    def fit(self, X, y, l_ind=None):
        """
        Provide an interface that can pass in multiple learners 
        or predictive results.

        Parameters
        ----------
        X : array-like
            Data matrix with [n_samples, n_features] or a set of prediction.

        y : array-like
            Each element is +1 or -1 for labeled instances. For unlabeled 
            instances, this parameter could be used for computing accuracy if 
            the ground truth is available.

        l_ind : array-like,optional(default=None)
            a row vector with length l, where l is the number of labeled
            instance. Each element is an index of a labeled instance.
        """

        N = X.shape[0]
        u_ind = np.linspace(0, N - 1, N).astype(np.int)
        u_ind = np.delete(u_ind, l_ind)

        self.prediction = np.zeros_like(y)
        self.prediction[l_ind] = y[l_ind]

        if self.estimator is False:
            self.fit_pred(X, y)
            self.prediction = self.Safer_prediction
        else:
            if l_ind is None:
                raise ValueError("Must provide label index")

            # XXX - Need to be Semi-supervised Regression??
            candidate_prediction1 = self.fit_estimator(
                X, y, l_ind, n_neighbors=3, metric='euclidean')
            candidate_prediction2 = self.fit_estimator(
                X, y, l_ind, n_neighbors=3, metric='cosine')
            candidate_prediction = np.hstack(
                [candidate_prediction1, candidate_prediction2])

            self.baseline_predict(X, y, l_ind)
            self.fit_pred(candidate_prediction, self.baseline_prediction)

            # print('baseline',self.baseline_prediction.shape)
            # print('safer_prediction',self.Safer_prediction.shape)
            self.prediction[u_ind] = self.Safer_prediction

    def fit_estimator(self, X, y, l_ind, n_neighbors=3, metric='minkowski'):
        """Provide a training interface that trains multiple models and give
        a safer prediction of these models.

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

        N = y.shape[0]
        u_ind = np.linspace(0, N - 1, N).astype(np.int)
        u_ind = np.delete(u_ind, l_ind)
        label_l = y[l_ind]
        unlabel_instance = X[u_ind]

        self.knn = KNeighborsClassifier(n_neighbors=n_neighbors, metric=metric,)

        self.knn.fit(X[l_ind], y[l_ind].ravel().astype('int'))

        [dist, idx] = self.knn.kneighbors(unlabel_instance)

        label_u = np.mean(np.array([y[i] for i in idx]).flatten().reshape(
            idx.shape[0], idx.shape[1]), axis=1)

        # instance = np.vstack((X, unlabel_instance))

        y = np.vstack((label_l, label_u.reshape(idx.shape[0], 1)))
        [dist, idx] = self.knn.kneighbors(unlabel_instance)

        for i in range(0, 5):
            label_u = np.mean(np.array([y[i] for i in idx]).flatten().reshape(
                idx.shape[0], idx.shape[1]), axis=1)
            # label_last = y
            y = np.vstack((label_l, label_u.reshape(idx.shape[0], 1)))

        Self_KNN_prediction = label_u.reshape(idx.shape[0], 1)
        return Self_KNN_prediction

    def baseline_predict(self, X, y, l_ind):
        """This is a  1NN regressor with euclidean distance measure.

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
        N = y.shape[0]
        u_ind = np.linspace(0, N - 1, N).astype(np.int)
        u_ind = np.delete(u_ind, l_ind)
        unlabel_instance = X[u_ind]

        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(X[l_ind], y[l_ind].ravel().astype('int'))
        [dist, idx] = knn.kneighbors(unlabel_instance)

        self.baseline_prediction = np.zeros((len(unlabel_instance), 1))
        for t in range(0, len(unlabel_instance)):
            self.baseline_prediction[t] = np.mean(
                np.array([y[i] for i in idx[t]]).flatten())

    def fit_pred(self, candidate_prediction=None, baseline_prediction=None):
        """SAFER implements the SAFER algorithm in [1].

        Parameters
        ----------
        candidate_prediction :array-like, optical(default=None)
            a matrix with size instance_num * candidate_num . Each
            column vector of candidate_prediction is a candidate regression 
            result.

        baseline_prediction :array-like, optical(default=None)
            a column vector with length instance_num. It is the regression
            result of the baseline method.

        Return
        ------
        Safer_prediction : array-like
            a predictive regression result by SAFER.

        """

        if candidate_prediction is None:
            raise ValueError("Please provide candidate prediction or "
                             "call the function that generates the prediction "
                             "result in this algorithm.")
        else:
            if baseline_prediction is None and self.baseline_prediction is None:
                raise ValueError("Please provide candidate prediction or "
                    "call the function that generates the prediction result "
                    "in this algorithm.")

        candidate_num = candidate_prediction.shape[1]

        H = np.dot(candidate_prediction.T, candidate_prediction) * 2
        f = -2 * np.dot(candidate_prediction.T, self.baseline_prediction)
        Aeq = np.ones((1, candidate_num))
        beq = 1.0

        lb = np.zeros((candidate_num, 1))
        ub = np.ones((candidate_num, 1))
        h = np.vstack((lb, ub))
        G_lb = -1 * np.eye(candidate_num, candidate_num)
        G_ub = np.eye(candidate_num, candidate_num)
        G = np.vstack((G_lb, G_ub))

        sln = solvers.qp(matrix(H), matrix(f), matrix(G), matrix(h),
                         matrix(Aeq), matrix(beq))
        x_value = sln['x']

        self.Safer_prediction = np.zeros((self.baseline_prediction.shape[0], 1))
        for i in range(0, candidate_num):
            self.Safer_prediction[:, 0] = self.Safer_prediction[:,
                0] + x_value[i] * candidate_prediction[:, i]

    def predict(self, u_ind):
        """Compute the most possible label for samples in X.

        Returns
        -------
        pred : array-like
            Each row is the most likely label for a sample [n_samples].
        """
        return self.prediction[u_ind]
