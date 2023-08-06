import numpy as np
from sklearn.semi_supervised import label_propagation
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.exceptions import ConvergenceWarning
from scipy import sparse

from ..base import TransductiveEstimatorwithGraph
from ..datasets.data_manipulate import check_y, modify_y
import warnings


class LPA(TransductiveEstimatorwithGraph):
    """Class for label propagation module.

    Parameters
    ----------
    kernel : {'knn', 'rbf', callable} (default='rbf')
        String identifier for kernel function to use or the kernel function
        itself. Only 'rbf' and 'knn' strings are valid inputs. The function
        passed should take two inputs, each of shape
        [n_samples, n_features], and return a [n_samples, n_samples] shaped
        weight matrix.

    gamma : float (default=20)
        Parameter for rbf kernel

    n_neighbors : integer > 0 (default=7)
        Parameter for knn kernel

    max_iter : integer (default=30)
        Change maximum number of iterations allowed

    tol : float (default=1e-3)
        Convergence tolerance: threshold to consider the system at steady
        state

    n_jobs : int or None, optional (default=None)
        The number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend`context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.
    """

    def __init__(self, kernel='rbf', gamma=20, n_neighbors=7,
                max_iter=30, tol=1e-3, n_jobs=None):

        super(LPA, self).__init__()
        self.max_iter = max_iter
        self.tol = tol

        # kernel parameters
        self.kernel = kernel
        self.gamma = gamma
        self.n_neighbors = n_neighbors

        self.n_jobs = n_jobs

        self.label_instance = []
        self.unlabel_instance = []
        self.label = []

        self.label_distributions = []
        self.transduction = []
        self.n_labels = None

    def set_params(self, param):
        """Parameter setting function.

        Parameters
        ----------
        param：dict
            Store parameter names and corresponding values {'name': value}.
        """
        if isinstance(param, dict):
            self.__dict__.update(param)
        self.label_instance = []
        self.unlabel_instance = []
        self.label = []

        self.label_distributions = []
        self.transduction = []
        self.n_labels = None

    def fit(self, X, y, labeled_idx, W):
        """Fit a label propagation model

        All the input data is provided matrix X (labeled and unlabeled)
        and corresponding label matrix y with a dedicated marker value for
        unlabeled samples. Optional matrix W is a graph provided for label 
        propagation.

        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]
            A {n_samples by n_samples} size matrix will be created from this

        y : array_like, shape = [n_samples]
            n_labeled_samples (unlabeled points are marked as 0)

        labeled_idx : array_like, shape = [n_samples]
            index of n_labeled_samples in X.

        W : array_like,  shape = [n_samples, n_samples]
            graph of instances

        Returns
        -------
        self : returns an instance of self.
        """
        self.n_labels, y = check_y(y, True)

        self.label_instance = X[labeled_idx]
        self.unlabel_instance = np.delete(X, labeled_idx, axis=0)

        instance = X
        if isinstance(X, sparse.spmatrix):
            labels = -np.ones(X.shape[0]).reshape(-1, 1)
        else:
            labels = -np.ones(len(X)).reshape(-1, 1)
        labels[labeled_idx] = y[labeled_idx] + 1
        self.label = labels

        if W is None:
            model = label_propagation.LabelPropagation(kernel=self.kernel,
                        gamma=self.gamma, n_neighbors=self.n_neighbors,
                        max_iter=self.max_iter, tol=self.tol,
                        n_jobs=self.n_jobs)
            model.fit(instance, labels)
            self.label_distributions = model.label_distributions_
            self.transduction = model.transduction_
        else:
            self._label_propagation(W, labels)

    def predict(self, index):
        """Performs transductive inference across the model.

        Parameters
        ----------
        index : array-like
            a row vector with length l, where l is the number of unlabeled
            instance. Each element is an index of a unlabeled instance.

        Returns
        -------
        y : array_like, shape = [n_samples]
            Predictions for input data
        """

        return modify_y(self.transduction.reshape(-1, 1) - 1,
                        index, self.n_labels)

    def _label_propagation(self, graph_matrix, y):
        """Performs label propagation given graph.

        Parameters
        ----------
        graph_matrix : array-like, shape = [n_samples, n_samples]
            A {n_samples by n_samples} size matrix will be created from this

        y : array_like, shape = [n_samples]
            graph of instances

        Returns
        -------
        y : array_like, shape = [n_samples]
            Predictions for input data
        """
        classes = np.unique(self.label)
        classes = (classes[classes != -1])
        self.classes = classes

        if isinstance(graph_matrix, sparse.spmatrix):
            n_samples = graph_matrix.shape[0]
        else:
            n_samples = len(graph_matrix)

        n_classes = len(classes)
        
        y = np.asarray(y)
        unlabeled = y.flatten() == -1

        # initialize distributions
        self.label_distributions = np.zeros((n_samples, n_classes))
        # print(self.label_distributions.shape)
        for label in classes:
            self.label_distributions[y.flatten() == label, classes == label] = 1

        y_static = np.copy(self.label_distributions)
        # if self._variant == 'propagation':
            # LabelPropagation
            # y_static[unlabeled] = 0
        # print(y_static)
        y_static[unlabeled] = 0
        # else:
            # LabelSpreading
        #    y_static *= 1 - alpha

        l_previous = np.zeros((n_samples, n_classes))

        unlabeled = unlabeled[:, np.newaxis]
        if sparse.isspmatrix(graph_matrix):
            graph_matrix = graph_matrix.tocsr()

        for self.n_iter_ in range(self.max_iter):
            if np.abs(self.label_distributions - l_previous).sum() < self.tol:
                break

            l_previous = self.label_distributions
            self.label_distributions = safe_sparse_dot(
                graph_matrix, self.label_distributions)

            # if self._variant == 'propagation':
            #    normalizer = np.sum(
            #        self.label_distributions, axis=1)[:, np.newaxis]
            #    self.label_distributions /= normalizer
            #    self.label_distributions = np.where(unlabeled,
            #    self.label_distributions, y_static)

            normalizer = np.sum(
            self.label_distributions, axis=1)[:, np.newaxis]
            self.label_distributions /= normalizer
            self.label_distributions = np.where(
                unlabeled, self.label_distributions, y_static)
            # else:
                # clamp
            #   self.label_distributions = np.multiply(
            #        alpha, self.label_distributions) + y_static
        else:
            warnings.warn(
                'max_iter=%d was reached without convergence.' % self.max_iter,
                category=ConvergenceWarning
            )
            self.n_iter_ += 1

        normalizer = np.sum(self.label_distributions, axis=1)[:, np.newaxis]
        self.label_distributions /= normalizer

        # set the transduction item
        transduction = self.classes[np.argmax(self.label_distributions,
                                               axis=1)]
        self.transduction = transduction.ravel()
