"""
S4VM implements the S4VM algorithm in [1].
-------------------------------------------
S4VM employs the Python version of libsvm [2] (available at
https://www.csie.ntu.edu.tw/~cjlin/libsvm/).

References
----------
..  [1] Yu-Feng Li and Zhi-Hua Zhou. Towards Making Unlabeled Data Never Hurt.
    In: Proceedings of the 28th International Conference on Machine Learning
    (ICML'11), Bellevue, Washington, 2011.

..  [2] R.-E. Fan, P.-H. Chen, and C.-J. Lin. Working set selection using 
    second order information for training SVM. Journal of Machine Learning 
    Research 6, 1889-1918, 2005.
"""
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import linprog
from sklearn.cluster import KMeans
from ..libs.svmutil import svm_train, svm_predict
from ..base import InductiveEstimatorWOGraph
from ..datasets.data_manipulate import check_y, modify_y


class S4VM(InductiveEstimatorWOGraph):
    """Base class for S4VM module.

    Parameters
    ----------
    kernel : 'RBF' or 'Linear' (default='RBF')
        String identifier for kernel function to use or the kernel function
        itself. Only 'RBF' and 'Linear' strings are valid inputs.

    gamma : float
        Parameter gamma is the width of RBF kernel. Default value is
        average distance between instances.

    C1 : double (default=100)
        Weight for the hinge loss of labeled instance.

    C2 : double (default=0.1)
        Weight for the hinge loss of unlabeled instance. If C2 is set as 0,
        our S4VM will degenerate to standard SVM.

    sampleTime : integer (default=100)
        The sampling times for each sampleTime.
    
    n_clusters : integer (default=10)
        The number of clusters to form as well as the number of centroids to 
        generate for K-means.
    """

    def __init__(self, kernel='RBF', C1=100, C2=0.1, sample_time=100, gamma=0,
                n_clusters=10):
        super(S4VM, self).__init__()
        # kernel parameters
        self.kernel = kernel
        self.gamma = gamma

        # weight parameters
        self.C1 = C1
        self.C2 = C2

        self.sample_time = sample_time
        self.n_clusters = n_clusters

        self.label_num = 0
        self.prediction = []
        self.y_svm = []
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

        self.label_num = 0
        self.prediction = []
        self.y_svm = []
        self.n_labels = None

    def fit(self, X, y, labeled_idx):
        """Fit the model according to the given training data.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            Training vector containing labeled and unlabeled instances, where 
            n_samples in the number of samples and n_features is the number of 
            features. All unlabeled samples will be transductively assigned 
            labels.

        y : array-like, shape = [n_labeled_samples]
            Target vector relative to labeled instances in X.

        labeled_idx : .array-like, shape = [n_labeled_samples]
            Index of labeled instances in X.

        Returns
        -------
        self : object
        """
        self.n_labels, y_ = check_y(y, binary=True)
        unlabeled_idx = np.linspace(
            0, y_.shape[0] - 1, y_.shape[0]).astype(np.int)
        unlabeled_idx = np.delete(unlabeled_idx, labeled_idx)

        unlabel_instance = np.delete(X, labeled_idx, axis=0)
        label_instance = X[labeled_idx, :]
        instance = np.row_stack((label_instance, unlabel_instance))

        # label_list = np.unique(y)
        # y = np.mean(label_list)

        label = y_[labeled_idx]
        self.label_num = np.size(label)
        unlabel_num = len(unlabel_instance)

        if self.kernel == 'RBF' and self.gamma == 0:
            dist = squareform(pdist(instance))
            # num = len(dist)
            self.gamma = np.sum(dist)

        C = np.row_stack((np.ones((self.label_num, 1)) * self.C1,
                         np.ones((unlabel_num, 1)) * self.C2))

        beta = np.sum(label) / np.size(label)
        alpha = 0.1
        cluster_num = int(self.sample_time / 10)
        Y = np.zeros((self.sample_time + 1, self.label_num + unlabel_num))
        S = np.zeros((self.sample_time + 1, 1))

        if self.kernel == 'Linear':
            model = svm_train(label.flatten(), label_instance, (np.ones(
                (self.label_num, 1)) * self.C1).flatten(), '-t 0')
        else:
            model = svm_train(label.flatten(), label_instance, 
                            (np.ones((self.label_num, 1)) * self.C1).flatten(),
                            '-g ' + str(self.gamma))
        self.y_svm = np.array(svm_predict(np.row_stack(
            (label, np.ones((unlabel_num, 1)))), instance, model)[0]).reshape(
                                                                        -1, 1)

        if np.sum(np.array(self.y_svm[self.label_num:self.label_num 
            + unlabel_num]) > 0) == 0 or np.sum(np.array(
            self.y_svm[self.label_num:self.label_num + unlabel_num]) < 0) == 0:
            Y = Y[0:self.sample_time, :]
            S = S[0:self.sample_time]
        else:
            predict_best, null, null, model_best = self._local_descent(
                instance, self.y_svm, self.label_num, unlabel_num,
                self.gamma, C, beta, alpha)
            Y[self.sample_time] = predict_best.reshape(-1)
            S[self.sample_time] = model_best.obj

        for i in range(0, self.sample_time):
            y_t = np.array(np.random.rand(unlabel_num, 1))
            if i <= self.sample_time * 0.8:
                y_t[y_t > 0.5] = 1
                y_t[y_t <= 0.5] = -1
                label_new = np.row_stack((label, y_t))
            else:
                y_t[y_t > 0.8] = -1
                y_t[y_t <= 0.8] = 1
                label_new = np.row_stack(
                    (label, y_t * np.array(self.y_svm).reshape(
                        -1, 1)[self.label_num:self.label_num + unlabel_num]))

            predict_best, null, null, model_best = self._local_descent(
                instance, label_new, self.label_num, unlabel_num,
                self.gamma, C, beta, alpha)

            Y[i] = predict_best.reshape(-1)
            S[i] = model_best.obj

        kmeans = KMeans(n_clusters=self.n_clusters).fit(Y)
        IDX = kmeans.predict(Y)
        D = kmeans.transform(Y)
        IDX = np.array(IDX).reshape((-1, 1))
        D = np.sum(D, 0)

        cluster_index = []
        for i in IDX:
            if i not in cluster_index:
                cluster_index.append(i)

        cluster_index = np.array(cluster_index).reshape(1, len(cluster_index))
        cluster_num = cluster_index.shape[1]

        prediction = np.zeros((self.label_num + unlabel_num, cluster_num))

        for i in range(0, cluster_num):
            index = np.array((IDX == cluster_index[0, i]).ravel().nonzero())
            temp_S = S[index][0]
            temp_Y = Y[index][0]
            index2 = temp_S.argmax(0)
            prediction[:, i] = temp_Y[index2, :][0]

        prediction_u_ind = self._linear_programming(
            prediction, self.y_svm, self.label_num, 3)

        self.prediction = np.zeros_like(y)
        self.prediction[labeled_idx] = y[labeled_idx]
        self.prediction[unlabeled_idx] = modify_y(
            prediction_u_ind.reshape(-1, 1), range(0, len(prediction_u_ind)),
            self.n_labels)

    def predict(self, u_ind):
        """Predict method replace the unsafe prediction with the baseline_pred 
        to improve the safeness.

        Parameters
        ----------
        u_ind : array-like
            a row vector with length l, where l is the number of unlabeled
            instance. Each element is an index of a unlabeled instance.

        Returns
        -------
        pred : a column vector with length n. Each element is a prediction for
            the label of the instance, including labeled and unlabeled
            instances, even though for labeled instances the prediction is
            consistent with the true label.
        """
        return np.array(self.prediction[u_ind]).reshape(-1, 1)

    def _linear_programming(self, yp, y_svm, label_num, lambda_):
        """Use linear programming to compute the best prediction of unlabeled instance.

        Parameters
        ----------
        yp : array-like
            predictions of unlabeled data in different clusters.
        y_svm : array-like
            predictions of unlabeled data by svm.
        label_num : int
            numbers of labeled data.
        lambda_: float
            lambda used to compute A and C.

        Returns
        -------
        label : array-like
            final predictions of unlabeled data.
        """
        yp = np.delete(yp, np.s_[0:label_num], axis=0)
        y_svm = np.delete(y_svm, np.s_[0:label_num], axis=0)
        (u, y_num) = yp.shape

        y_svm = np.array(y_svm).reshape(-1, 1)
        A = np.column_stack((np.ones((y_num, 1)), ((
            1 - lambda_) * np.kron(np.ones((1, y_num)), y_svm) / 4 - (
                                                    1 + lambda_) * yp / 4).T))
        C = np.ones((y_num, 1)) * (1 - lambda_) * u / 4 - \
                    ((1 + lambda_) * yp.T).dot(y_svm / 4)
        g = np.row_stack((-1, np.zeros((u, 1)))).flatten()
        lb = np.row_stack((None, -np.ones((u, 1))))
        ub = np.row_stack((None, np.ones((u, 1))))
        bounds = []
        for i in range(0, len(lb)):
            bounds.append((lb[i][0], ub[i][0]))
        prediction = linprog(c=g, A_ub=A, b_ub=C,
                             bounds=bounds, options={"tol": 1e-11}).x
        if prediction[0] < 0:
            label = y_svm
        else:
            prediction = np.delete(prediction, 0, axis=0)
            label = np.sign(prediction)
        return label

    def _local_descent(self, instance, label, label_num, unlabel_num, gamma,
                        C, beta, alpha):
        """Perform S3VM to find the best separator.

        Parameters
        ----------
        instance : array-like
            all instances.
        label : array-like
            labels of instances.
        label_num : int
            numbers of labeled instances.
        unlabel_num : int 
            numbers of unlabeled instances.
        gamma : float
            parameter of RBF.
        C : float
            weight of labeled and unlabeled instances.
        beta : float
            parameter of S3VM.
        alpha : float
            parameter of S3VM.

        Returns 
        -------
        predict_label : array-like
            predictions of labeled instances.
        acc : float
            accuracy of predictions.
        values : float
            objective value.
        model : class
            best model of S3VM.
        """
        predict_label_last_last = np.array(label)
        if gamma == 0:
            model = svm_train(predict_label_last_last.flatten(),
                              instance, C.flatten(), '-t 0')
        else:
            model = svm_train(predict_label_last_last.flatten(),
                              instance, C.flatten(), '-g ' + str(gamma))
        predict_label, acc, values = svm_predict(
            predict_label_last_last, instance, model)

        if values[0][0] * predict_label[0] < 0:
            values = -values

        values_sort = np.sort(np.array(values).flatten())[::-1]
        index = np.argsort(np.array(values).flatten())[::-1]
        h1 = int(np.ceil((label_num + unlabel_num) * (1 + beta - alpha) / 2))
        h2 = int(np.ceil((label_num + unlabel_num) * (1 - beta - alpha) / 2))

        predict_label = np.array(predict_label)
        predict_label[index[0:h1]] = 1
        predict_label[index[label_num + unlabel_num 
            - h2 + 1:label_num + unlabel_num]] = -1
        values_sort = values_sort[h1:(label_num + unlabel_num - h2)]
        predict_label[index[np.array(
            (values_sort >= 0).ravel().nonzero()) + h1]] = 1
        predict_label[index[np.array(
            (values_sort < 0).ravel().nonzero()) + h1]] = -1
        predict_label_last = predict_label
        model_last = model

        num = int(np.ceil(unlabel_num * 0.2))
        index = np.random.permutation(unlabel_num)
        index = index[0:num]
        change = np.ones((unlabel_num, 1))
        change[index] = 0
        change = np.row_stack((np.ones((label_num, 1)), change))

        stop = 0
        num_iterative = 0
        predict_label_last = np.array(predict_label_last).reshape(-1, 1)
        predict_label_last_last = np.array(
            predict_label_last_last).reshape(-1, 1)
        while stop == 0:
            label_new = change * predict_label_last + \
                (1 - change) * predict_label_last_last
            if gamma == 0:
                model = svm_train(label_new.flatten(),
                                  instance, C.flatten(), '-t 0')
            else:
                model = svm_train(label_new.flatten(), instance,
                                  C.flatten(), '-g ' + str(gamma))
            predict_label, acc, values = svm_predict(label_new, instance, model)
            predict_label = np.array(predict_label).reshape(-1, 1)
            num_iterative = num_iterative + 1
            if values[0][0] * predict_label[0] < 0:
                values = -values
            values_sort = np.sort(np.array(values).flatten())[::-1]
            index = np.argsort(np.array(values).flatten())[::-1]
            predict_label[index[0:h1]] = 1
            predict_label[index[label_num + unlabel_num
                - h2:label_num + unlabel_num]] = -1
            values_sort = values_sort[h1:(label_num + unlabel_num - h2)]
            predict_label[index[np.array(
                (values_sort >= 0).ravel().nonzero()) + h1]] = 1
            predict_label[index[np.array(
                (values_sort < 0).ravel().nonzero()) + h1]] = -1

            if ((np.array(predict_label) == np.array(
                    predict_label_last)).sum(axis=0) == label_num + unlabel_num 
                    and round(model.obj, 4) == round(model_last.obj, 4)
                    or num_iterative > 200):
                stop = 1
            else:
                model_last = model
                predict_label_last_last = predict_label_last
                predict_label_last = predict_label

                num = int(np.ceil(unlabel_num * 0.2))
                index = np.random.permutation(unlabel_num)
                index = index[0:num]
                change = np.ones((unlabel_num, 1))
                change[index] = 0
                change = np.row_stack((np.ones((label_num, 1)), change))
        return predict_label, acc, values, model
