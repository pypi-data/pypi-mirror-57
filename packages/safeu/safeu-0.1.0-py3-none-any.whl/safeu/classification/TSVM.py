#
import numpy as np
from scipy.spatial.distance import pdist, squareform
from ..libs.svmutil import svm_train, svm_predict
from ..base import InductiveEstimatorWOGraph
from ..datasets.data_manipulate import check_y, modify_y


class TSVM(InductiveEstimatorWOGraph):
    """TSVM classifier

    Parameters
    ----------
    kernel : {'Linear', 'RBF'} (default='RBF')
        String identifier for kernel function to use or the kernel function
        itself. Only 'Linear' and 'RBF' strings are valid inputs.

    C1 : float (default=100)
        Initial weight for labeled instances.

    C2 : float (default=0.1)
        Initial weight for unlabeled instances.

    alpha : float (default=0.1)
        Balance parameter

    beta : float (default=-1)
        Balance parameter

    gamma : float (default=0)
        Parameter for RBF kernel


    Other Parameters
    ----------------
    model : object
        Best model.
    """

    def __init__(self, kernel='RBF', C1=100, C2=0.1, alpha=0.1, beta=-1,
                 gamma=0):
        # super(TSVM, self).__init__()
        self.kernel = kernel
        self.C1 = C1
        self.C2 = C2
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        self.model = None
        self.n_labels = None

    def __getstate__(self):
        """
        The model is ctypes objects and contains pointers cannot be pickled.
        So we drop the model when we pickle TSVM.
        """
        state = self.__dict__.copy()
        del state['model']  # manually delete
        return state

    def __setstate__(self, state):
        """
        The model is ctypes objects and contains pointers cannot be pickled.
        So we drop the model when we pickle TSVM.
        """
        self.__dict__.update(state)
        self.model = None  # manually update

    def set_params(self, param):
        """Parameter setting function.

        Parameters
        ----------
        param：dict
            Store parameter names and corresponding values {'name': value}.
        """
        if isinstance(param, dict):
            self.__dict__.update(param)

        self.model = None
        self.n_labels = None

    def fit(self, X, y, labeled_idx):
        """Fit a semi-supervised SVM model

        All the input data is provided matrix X (labeled and unlabeled)
        and corresponding label matrix y with a dedicated marker value for
        unlabeled samples.

        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]
            A {n_samples by n_samples} size matrix will be created from this

        y : array_like, shape = [n_samples]
            n_labeled_samples (unlabeled points are marked as 0)

        labeled_idx : array_like, shape = [n_samples]
            index of n_labeled_samples in X.

        Returns
        -------
        self : returns an instance of self.
        """
        self.n_labels, y_ = check_y(y, binary=True)
        unlabel_instance = np.delete(X, labeled_idx, axis=0)
        label_instance = X[labeled_idx, :]
        label_num = np.size(labeled_idx)
        unlabel_num = len(unlabel_instance)
        instance = np.row_stack((label_instance, unlabel_instance))
        labels = y_.reshape((-1, 1))

        if self.kernel == 'Linear':
            model = svm_train(labels[labeled_idx].flatten(), label_instance,
                              (np.ones((label_num, 1)) * self.C1).flatten(),
                              '-t 0')
        else:
            model = svm_train(labels[labeled_idx].flatten(), label_instance,
                              (np.ones((label_num, 1)) * self.C1).flatten(),
                              '-g ' + str(self.gamma))
        label = np.array(svm_predict(np.row_stack((labels[labeled_idx],
                                                   np.ones((unlabel_num, 1)))),
                                     instance, model)[0]).reshape(-1, 1)

        if self.beta == -1:
            self.beta = np.sum(label) / np.size(label)
        if self.kernel == 'RBF' and self.gamma == 0:
            dist = squareform(pdist(instance))
            num = len(dist)
            self.gamma = np.sum(dist)

        C = np.row_stack((np.ones((label_num, 1)) * self.C1,
                         np.ones((unlabel_num, 1)) * self.C2))

        predict_label_last_last = np.array(label)
        if self.gamma == 0:
            model = svm_train(predict_label_last_last.flatten(),
                              instance, C.flatten(), '-t 0')
        else:
            model = svm_train(predict_label_last_last.flatten(
            ), instance, C.flatten(), '-g ' + str(self.gamma))
        predict_label, acc, values = svm_predict(
            predict_label_last_last, instance, model)

        if values[0][0] * predict_label[0] < 0:
            values = -np.array(values)

        values_sort = np.sort(np.array(values).flatten())[::-1]
        index = np.argsort(np.array(values).flatten())[::-1]
        h1 = int(np.ceil((label_num + unlabel_num)
                 * (1 + self.beta - self.alpha) / 2))
        h2 = int(np.ceil((label_num + unlabel_num)
                 * (1 - self.beta - self.alpha) / 2))

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
            if self.gamma == 0:
                model = svm_train(label_new.flatten(), instance, C.flatten(),
                                  '-t 0')
            else:
                model = svm_train(label_new.flatten(), instance,
                                  C.flatten(), '-g ' + str(self.gamma))
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

            if (np.array(predict_label) == np.array(predict_label_last)).sum(
                    axis=0) == label_num + unlabel_num and round(model.obj, 6)\
                    == round(model_last.obj, 6) or num_iterative > 200:
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
        self.model = model

    def predict(self, X):
        """Performs inductive inference across the model.

        Parameters
        ----------
        X : array_like, shape = [n_samples, n_features]

        Returns
        -------
        y : array_like, shape = [n_samples]
            Predictions for input data
        """
        res = np.array(svm_predict(x=X, y=np.ones(
            len(X)), m=self.model)[0]).reshape(-1, 1)
        return modify_y(res, range(0, len(res)), self.n_labels)
