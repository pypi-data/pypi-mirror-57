"""
Base IO code for all datasets
"""

from __future__ import print_function

import shutil
from os import environ, makedirs
from os.path import dirname, exists, expanduser, join
import hashlib
import scipy.sparse as sp
import scipy.io as sio
import h5py
from sklearn.utils import Bunch
import numpy as np
import pandas as pd
from .usps import load_usps
from .covtype import load_covtype, load_graph_covtype

import six.moves.urllib.request


__all__ = ['get_data_home',
           'clear_data_home',
           'load_data',
           'load_graph',
           'load_boston',
           'load_diabetes',
           'load_digits',
           'load_iris',
           'load_breast_cancer',
           'load_linnerud',
           'load_wine',
           'load_ionosphere',
           'load_australian',
           'load_bupa',
           'load_haberman',
           'load_vehicle',
           'load_covtype',
           'load_spambase',
           'load_house',
           'load_clean1',
           'load_dataset',
           'load_usps',
           'load_graph_covtype',
           ]

dataset_list = ['boston', 'diabetes', 'digits', 'iris', 'breast_cancer',
                'linnerud', 'wine', 'ionosphere', 'australian', 'bupa',
                'haberman', 'vehicle', 'covtype', 'spambase', 'house',
                'clean1', 'usps', 'isolet']

graph_list = ['covtype']

DEBUG = False


def get_data_home(data_home=None):
    """Return the path of the data dir.

    This folder is used by some large dataset loaders to avoid downloading the
    data several times.

    If the folder does not already exist, it is automatically created.

    Parameters
    ----------
    data_home : str | None
        The path to data dir.
    """
    if data_home is None:
        data_home = environ.get('DATA', join('~', 'data'))
    data_home = expanduser(data_home)
    if not exists(data_home):
        makedirs(data_home)
    return data_home


def clear_data_home(data_home=None):
    """Delete all the content of the data home cache.

    Parameters
    ----------
    data_home : str | None
        The path to data dir.
    """
    data_home = get_data_home(data_home)
    shutil.rmtree(data_home)


def _sha256(path):
    """Calculate the sha256 hash of the file at path.
    
    Parameters
    ----------
    path : str
        The path of the file.

    Returns
    -------
    hash : The sha256 hash of the file at path.
    """
    sha256hash = hashlib.sha256()
    chunk_size = 8192
    with open(path, "rb") as f:
        while True:
            buffer = f.read(chunk_size)
            if not buffer:
                break
            sha256hash.update(buffer)
    return sha256hash.hexdigest()


def _fetch_remote(remote, dirname=None):
    """Fetch a dataset pointed by remote's url, save into path using remote's
    filename and ensure its integrity based on the SHA256 Checksum of the
    downloaded file.

    Parameters
    -----------
    remote : RemoteFileMetadata
        Named tuple containing remote dataset meta information: url, filename
        and checksum

    dirname : string
        Directory to save the file to.

    Returns
    -------
    file_path : string
        Full path of the created file.
    """

    file_path = (remote.filename if dirname is None
                 else join(dirname, remote.filename))
    six.moves.urllib.request.urlretrieve(remote.url, file_path)

    checksum = _sha256(file_path)
    if remote.checksum != checksum:
        raise IOError("{} has an SHA256 checksum ({}) "
                      "differing from expected ({}), "
                      "file may be corrupted.".format(file_path, checksum,
                                                      remote.checksum))
    return file_path


def load_graph(name, graph_file=None):
    """
    Load graph from self-contained data set or user-provided data set.
    The self-contained data set is loaded first according to the provided data 
    set name. Load the dataset according to the provided path when the dataset 
    name is empty or does not exist.

    Parameters
    ----------
    name : string.optional (default=None)
        Name should be the name of the data in the self-contained data list.

    graph_file : string.optional (default=None)
        The absolute path of the user-provided feature dataset.
        The File should be in '*.csv/mat/npz' format .

    Returns
    -------
    W : np.nda
    """
    if name is not None:
        if name in graph_list:
            W = eval('load_graph_' + name)(True)
        else:
            if graph_file is not None:
                W = load_graph_diff_formats(graph_file)
            else:
                return None
    else:
        if graph_file is not None:
            W = load_graph_diff_formats(graph_file)
        else:
            return None

    return W


def load_graph_diff_formats(graph_file=None):
    """Load graph from `*.csv/mat/npz`

    Parameters
    ----------
    graph_file : string
        Absolute path to the graph file

    Return
    ------
    W : np.nda
    """
    if not graph_file:
        return None

    if graph_file.endswith('csv'):
        df = pd.read_csv(graph_file)
        W = df.as_matrix(columns=None)  # np.ndarray
    elif graph_file.endswith('mat'):
        # if version <= 7.2
        try:
            data = sio.loadmat(graph_file)
            W = data['W']

        # mat version >= 7.3
        except NotImplementedError:
            try:
                data = h5py.File(graph_file)
                # W = data['W'].value.T
                W = data['W'][()].T

            except NotImplementedError:  # XXX: test?
                raise IOError('Can not open .mat file.')

    # sparse matrix   <class 'scipy.sparse.csc.csc_matrix'>
    elif graph_file.endswith('npz'):
        W = sp.load_npz(graph_file)
    else:
        raise ValueError("Not supported file type. Should be *.csv/npz/mat")

    return W


def load_dataset(name=None, feature_file=None, label_file=None):
    """Load data from self-contained data set or user-provided data set.
    The self-contained data set is loaded first according to the provided data 
    set name. Load the dataset according to the provided path when the dataset 
    name is empty or does not exist.

    Parameters
    ----------
    name : string.optional (default=None)
        Name should be the name of the data in the self-contained data list.

    feature_file : string.optional (default=None)
       The absolute path of the user-provided feature dataset.
       The File should be in '.csv' format and organized as follows:

       =============   ==============
       feature_name:   [1,n_features]
       data:            [m_samples,n]
       =============   ==============

    label_file : string.optional (default=None)
       The absolute path of the user-provided label dataset.
       The File should be in '.csv' format and organized as follows:

       =============   ==============
       label_name:       [1,n_labels]
       label:           [m_samples,n]
       =============   ==============

       Besides,the number of rows in the label_file should be the same as
       the feature_file.

    Returns
    -------
    X : array-like
       Data matrix with [m_samples, n_features].The data will be used to
       train models.

    y : array-like
       The label of load data with [m_samples, n_labels].
    """
    if name is not None:
        if name in dataset_list:
            X, y = eval('load_' + name)(True)
        else:
            if feature_file is None and label_file is None:
                raise ValueError("The dataset is not found.")
            else:
                X, y = load_data(feature_file, label_file)
    else:
        X, y = load_data(feature_file, label_file)

    return X, y


def load_data(feature_file=None, label_file=None):
    """Load data from absolute path.

    Parameters
    ----------
    feature_file : string.optional (default=None)
       The absolute path of the user-provided feature dataset.
       The File should be in '.csv' format and organized as follows:

       =============   ==============
       feature_name:   [1,n_features]
       data:            [m_samples,n]
       =============   ==============

       When the feature is a sparse matrix, the file should be in '*./mat/npz' 
       format.

    label_file : string.optional (default=None)
       The absolute path of the user-provided label dataset.
       The File should be in '.csv' format and organized as follows:

       =============   ==============
       label_name:       [1,n_labels]
       label:           [m_samples,n]
       =============   ==============

       When the label is a sparse matrix, the file should be in '*./mat/npz' 
       format.

       Besides,the number of rows in the label_file should be the same as
       the feature_file.

    Returns
    -------
    X : array-like
       Data matrix with [m_samples, n_features].The data will be used to
       train models.

    y : array-like
       The label of load data with [m_samples, n_labels].
    """
    if feature_file is None and label_file is None:
        raise Exception(
            "Must provide data name or feature file and label file.")
    elif (feature_file is None and label_file is not None) or \
            (feature_file is not None and label_file is None):
        raise Exception("Must provide both of feature file and label file.")
    else:
        if feature_file.endswith('csv'):
            with open(feature_file, encoding='utf-8') as f:
                X = pd.read_csv(f, delimiter=',', low_memory=False).get_values()
        else:
            X = load_graph_diff_formats(feature_file)

        if label_file.endswith('csv'):
            with open(label_file, encoding='utf-8') as f:
                y = pd.read_csv(f, delimiter=',', low_memory=False).get_values()
        else:
            y = load_graph_diff_formats(label_file)

        assert X.shape[0] == y.shape[0]
        if DEBUG:
            print(X.shape)
            print(y.shape)
    return X, y


def load_digits(return_X_y=False):
    """Load and return the digits dataset (classification).

    Each datapoint is a 8x8 image of a digit.

    =================   ==============
    Classes                         10
    Samples per class             ~180
    Samples total                 1797
    Dimensionality                  64
    Features             integers 0-16
    =================   ==============

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.


    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        'data', the data to learn, 'images', the images corresponding
        to each sample, 'target', the classification labels for each
        sample, 'target_names', the meaning of the labels, and 'DESCR',
        the full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True


    This is a copy of the test set of the UCI ML hand-written digits datasets
    http://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits
    """
    n_class = 10

    module_path = dirname(__file__)
    data = np.loadtxt(join(module_path, 'data', 'digits.csv.gz'),
                      delimiter=',')
    with open(join(module_path, 'descr', 'digits.rst')) as f:
        descr = f.read()
    target = data[:, -1].astype(np.int)
    target = np.reshape(target, (data.shape[0], 1))

    flat_data = data[:, :-1]
    images = flat_data.view()
    images.shape = (-1, 8, 8)

    if n_class < 10:
        idx = target < n_class
        flat_data, target = flat_data[idx], target[idx]
        images = images[idx]

    if return_X_y:
        return flat_data, target

    return Bunch(data=flat_data,
                 target=target,
                 target_names=np.arange(10),
                 images=images,
                 DESCR=descr)


def load_iris(return_X_y=False):
    """Load and return the iris dataset (classification).

    The iris dataset is a classic and very easy multi-class classification
    dataset.

    =================   ==============
    Classes                          3
    Samples per class               50
    Samples total                  150
    Dimensionality                   4
    Features            real, positive
    =================   ==============

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object. See
        below for more information about the `data` and `target` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        'data', the data to learn, 'target', the classification labels,
        'target_names', the meaning of the labels, 'feature_names', the
        meaning of the features, and 'DESCR', the
        full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True

    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'iris')
    data, target = load_data(join(base_dir, 'iris_feature.csv'),
                             join(base_dir, 'iris_label.csv'))

    with open(join(module_path, 'descr', 'iris.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target,
                 target_names=['setosa', 'versicolor', 'virginica'],
                 DESCR=fdescr,
                 feature_names=['sepal length (cm)', 'sepal width (cm)',
                                'petal length (cm)', 'petal width (cm)'])


def load_breast_cancer(return_X_y=False):
    """Load and return the breast cancer wisconsin dataset (classification).

    The breast cancer dataset is a classic and very easy binary classification
    dataset.

    =================   ==============
    Classes                          2
    Samples per class    212(M),357(B)
    Samples total                  569
    Dimensionality                  30
    Features            real, positive
    =================   ==============

    Parameters
    ----------
    return_X_y : boolean, default=False
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.


    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        'data', the data to learn, 'target', the classification labels,
        'target_names', the meaning of the labels, 'feature_names', the
        meaning of the features, and 'DESCR', the
        full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True


    The copy of UCI ML Breast Cancer Wisconsin (Diagnostic) dataset is
    downloaded from: https://goo.gl/U2Uwz2
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'breast_cancer')
    data, target = load_data(join(base_dir, 'breast_cancer_feature.csv'),
                             join(base_dir, 'breast_cancer_label.csv'))

    with open(join(module_path, 'descr', 'breast_cancer.rst')) as rst_file:
        fdescr = rst_file.read()

    feature_names = np.array(['mean radius', 'mean texture',
                              'mean perimeter', 'mean area',
                              'mean smoothness', 'mean compactness',
                              'mean concavity', 'mean concave points',
                              'mean symmetry', 'mean fractal dimension',
                              'radius error', 'texture error',
                              'perimeter error', 'area error',
                              'smoothness error', 'compactness error',
                              'concavity error', 'concave points error',
                              'symmetry error', 'fractal dimension error',
                              'worst radius', 'worst texture',
                              'worst perimeter', 'worst area',
                              'worst smoothness', 'worst compactness',
                              'worst concavity', 'worst concave points',
                              'worst symmetry', 'worst fractal dimension'])

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target,
                 target_names=['malignant', 'benign'],
                 DESCR=fdescr,
                 feature_names=feature_names)


def load_linnerud(return_X_y=False):
    """Load and return the linnerud dataset (multivariate regression).

    ==============    ============================
    Samples total     				20
    Dimensionality    3 (for both data and target)
    Features          			   integer
    Targets           			   integer
    ==============    ============================

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are: 'data' and
        'targets', the two multivariate datasets, with 'data' corresponding to
        the exercise and 'targets' corresponding to the physiological
        measurements, as well as 'feature_names' and 'target_names'.

    (data, target) : tuple if ``return_X_y`` is True

    """
    base_dir = join(dirname(__file__), 'data', 'linnerud/')
    # Read data
    data_exercise = np.loadtxt(base_dir + 'linnerud_exercise.csv', skiprows=1)
    data_physiological = np.loadtxt(base_dir + 'linnerud_physiological.csv',
                                    skiprows=1)
    # Read header
    with open(base_dir + 'linnerud_exercise.csv') as f:
        header_exercise = f.readline().split()
    with open(base_dir + 'linnerud_physiological.csv') as f:
        header_physiological = f.readline().split()
    with open(dirname(__file__) + '/descr/linnerud.rst') as f:
        descr = f.read()

    if return_X_y:
        return data_exercise, data_physiological

    return Bunch(data=data_exercise, feature_names=header_exercise,
                 target=data_physiological,
                 target_names=header_physiological,
                 DESCR=descr)


def load_boston(return_X_y=False):
    """Load and return the boston house-prices dataset (regression).

    ==============     ==============
    Samples total                 506
    Dimensionality                 13
    Features           real, positive
    Targets             real 5. - 50.
    ==============     ==============

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        'data', the data to learn, 'target', the regression targets,
        and 'DESCR', the full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True
    """
    module_path = dirname(__file__)

    fdescr_name = join(module_path, 'descr', 'boston_house_prices.rst')
    with open(fdescr_name) as f:
        descr_text = f.read()

    base_dir = join(module_path, 'data', 'boston')
    data, target = load_data(join(base_dir, 'boston_house_prices_feature.csv'),
                             join(base_dir, 'boston_house_prices_label.csv'))

    if return_X_y:
        return data, target

    return Bunch(data=data,
                 target=target,
                 # last column is target value
                 feature_names=["CRIM", "ZN", "INDUS",
                                "CHAS", "NOX", "RM",
                                "AGE", "DIS", "RAD",
                                "TAX", "PTRATIO", "B",
                                "LSTAT"],
                 DESCR=descr_text)


def load_wine(return_X_y=False):
    """Load and return the wine dataset (classification).

    The wine dataset is a classic and very easy multi-class classification
    dataset.

    =================   ==============
    Classes                          3
    Samples per class       [59,71,48]
    Samples total                  178
    Dimensionality                  13
    Features            real, positive
    =================   ==============

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are: 'data', the
        data to learn, 'target', the classification labels, 'target_names', the
        meaning of the labels, 'feature_names', the meaning of the features,
        and 'DESCR', the full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True


    The copy of UCI ML Wine Data Set dataset is downloaded and modified to fit
    standard format from:
    https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'wine')
    data, target = load_data(join(base_dir, 'wine_feature.csv'),
                             join(base_dir, 'wine_label.csv'))

    with open(join(module_path, 'descr', 'wine.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target,
                 target_names=['class_0', 'class_1', 'class_2'],
                 DESCR=fdescr,
                 feature_names=['alcohol',
                                'malic_acid',
                                'ash',
                                'alcalinity_of_ash',
                                'magnesium',
                                'total_phenols',
                                'flavanoids',
                                'nonflavanoid_phenols',
                                'proanthocyanins',
                                'color_intensity',
                                'hue',
                                'od280/od315_of_diluted_wines',
                                'proline'])


def load_diabetes(return_X_y=False):
    """Load and return the diabetes dataset (regression).

    ==============      ==================
    Samples total                      442
    Dimensionality                      10
    Features            real, -.2 < x < .2
    Targets               integer 25 - 346
    ==============      ==================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        'data', the data to learn and 'target', the regression target for each
        sample.

    (data, target) : tuple if ``return_X_y`` is True
    """

    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'diabetes')
    data = np.loadtxt(join(base_dir, 'diabetes_feature.csv.gz'))
    target = np.loadtxt(join(base_dir, 'diabetes_label.csv.gz'))
    target = np.reshape(target, (data.shape[0], 1)).astype(int)

    with open(join(module_path, 'descr', 'diabetes.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=['age', 'sex', 'bmi', 'bp',
                                's1', 's2', 's3', 's4', 's5', 's6'])


def load_ionosphere(return_X_y=False):
    """Load and return the ionosphere dataset (classification).

    The ionosphere dataset is a classic and very easy multi-class classification
    dataset.

    =================   ==============
    Classes                          2
    Samples per class        [225,126]
    Samples total                  351
    Dimensionality                  34
    Features                 good, bad
    =================   ==============

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are: 'data', the
        data to learn, 'target', the classification labels, 'target_names', the
        meaning of the labels, 'feature_names', the meaning of the features,
        and 'DESCR', the full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True


    The copy of UCI ML ionosphere Data Set dataset is downloaded and modified 
    to fit standard format from:
    https://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'ionosphere')
    data, target = load_data(join(base_dir, 'ionosphere_feature.csv'),
                             join(base_dir, 'ionosphere_label.csv'))

    with open(join(module_path, 'descr', 'ionosphere.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target,
                 target_names=['good', 'bad'],
                 DESCR=fdescr,
                 feature_names=[])


def load_australian(return_X_y=False):
    """Load and return the australian dataset (classification).

    The australian dataset is a classic and very easy multi-class classification
    dataset.

    =================   ================
    Classes                            2
    Samples per class          [383,307]
    Samples total                    690
    Dimensionality                    14
    Features            class_0, class_1
    =================   ================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are: 'data', the
        data to learn, 'target', the classification labels, 'target_names', the
        meaning of the labels, 'feature_names', the meaning of the features,
        and 'DESCR', the full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True


    The copy of UCI ML australian Data Set dataset is downloaded and modified 
    to fit standard format from:
    https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/australian/australian.dat
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'australian')
    data, target = load_data(join(base_dir, 'australian_feature.csv'),
                            join(base_dir, 'australian_label.csv'))

    with open(join(module_path, 'descr', 'australian.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target,
                 target_names=['class_0', 'class_1'],
                 DESCR=fdescr,
                 feature_names=[])


def load_bupa(return_X_y=False):
    """Load and return the bupa dataset (classification).

    The bupa dataset is a classic and very easy multi-class classification
    dataset.

    =================   =================
    Classes                             2
    Samples per class           [200,145]
    Samples total                     345
    Dimensionality                      6
    Features             class_0, class_1
    =================   =================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are: 'data', the
        data to learn, 'target', the classification labels, 'target_names', the
        meaning of the labels, 'feature_names', the meaning of the features,
        and 'DESCR', the full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True


    The copy of UCI ML bupa Data Set dataset is downloaded and modified to fit
    standard format from:
    https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/bupa.data
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'bupa')
    data, target = load_data(join(base_dir, 'bupa_feature.csv'),
                             join(base_dir, 'bupa_label.csv'))

    with open(join(module_path, 'descr', 'bupa.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target,
                 target_names=['class_1', 'class_2'],
                 DESCR=fdescr,
                 feature_names=['mcv', 'alkphos', 'sgpt',
                                'sgot', 'gammagt', 'drinks'])


def load_haberman(return_X_y=False):
    """Load and return the haberman dataset (classification).

    The haberman dataset is a classic and very easy multi-class classification
    dataset.

    =================  =================
    Classes                            2
    Samples per class           [225,81]
    Samples total                    306
    Dimensionality                     3
    Features            class_0, class_1
    =================  =================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(X, y)`` instead of a Bunch object.
        See below for more information about the `X` and `y` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are: 'data', the
        data to learn, 'target', the classification labels, 'target_names', the
        meaning of the labels, 'feature_names', the meaning of the features,
        and 'DESCR', the full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True


    The copy of UCI ML haberman Data Set dataset is downloaded and modified to 
    fit standard format from:
    https://archive.ics.uci.edu/ml/machine-learning-databases/haberman/haberman.data
    """

    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'haberman')
    data, target = load_data(join(base_dir, 'haberman_feature.csv'),
                             join(base_dir, 'haberman_label.csv'))

    with open(join(module_path, 'descr', 'haberman.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target,
                 target_names=['survived_5_years_or_longer',
                     'died_within_5_year'],
                 DESCR=fdescr,
                 feature_names=[
                     'Age', 'year - 1900', 'positive axillary nodes'])


def load_vehicle(return_X_y=False):
    """Load and return the vehicle dataset (classification).

    The vehicle dataset is a classic and very easy multi-class classification
    dataset.

    =================   ==================================
    Classes                                              4
    Samples per                     class[137,148,168,143]
    Samples total                                      596
    Dimensionality                                      18
    Features             class_0, class_1,class_2, class_3
    =================   ==================================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are: 'data', the
        data to learn, 'target', the classification labels, 'target_names', the
        meaning of the labels, 'feature_names', the meaning of the features,
        and 'DESCR', the full description of the dataset.

    (data, target) : tuple if ``return_X_y`` is True


    The copy of libsvm vehicle Data Set dataset is downloaded and modified to 
    fit standard format from:
    https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass/vehicle.scale

    Besides,We dropped the missing data.
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'vehicle')
    data, target = load_data(join(base_dir, 'vehicle_feature.csv'),
                             join(base_dir, 'vehicle_label.csv'))

    with open(join(module_path, 'descr', 'vehicle.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=[])


def load_spambase(return_X_y=False):
    """Load and return the spambase dataset (classification).

    The spambase dataset is a classic and very easy multi-class classification
    dataset.

    =================   =================
    Classes                             2
    Samples per          class[1813,2788]
    Samples total                    4601
    Dimensionality                     57
    Features             class_0, class_1
    =================   =================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=True.
        If True, returns ``(data, target)`` .
        See below for more information about the `data` and `target` object.

    Returns
    -------
    (data, target) : tuple if ``return_X_y`` is True
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'spambase')
    data, target = load_data(join(base_dir, 'spambase_feature.csv'),
                             join(base_dir, 'spambase_label.csv'))

    with open(join(module_path, 'descr', 'spambase.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target
    
    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=[])


def load_house(return_X_y=False):
    """Load and return the house dataset (classification).

    The spambase dataset is a classic and very easy multi-class classification
    dataset.

    =================   =================
    Classes                             2
    Samples per            class[108,124]
    Samples total                     232
    Dimensionality                     16
    Features             class_0, class_1
    =================   =================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=True.
        If True, returns ``(data, target)`` .
        See below for more information about the `data` and `target` object.

    Returns
    -------
    (data, target) : tuple if ``return_X_y`` is True
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'house')
    data, target = load_data(join(base_dir, 'house_feature.csv'),
                             join(base_dir, 'house_label.csv'))

    with open(join(module_path, 'descr', 'house.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target
    
    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=[])


def load_clean1(return_X_y=False):
    """Load and return the clean1 dataset (classification).

    The spambase dataset is a classic and very easy multi-class classification
    dataset.

    =================   =================
    Classes                             2
    Samples per            class[207,269]
    Samples total                     476
    Dimensionality                    166
    Features             class_0, class_1
    =================   =================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=True.
        If True, returns ``(data, target)`` .
        See below for more information about the `data` and `target` object.

    Returns
    -------
    (data, target) : tuple if ``return_X_y`` is True
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'clean1')
    data, target = load_data(join(base_dir, 'clean1_feature.csv'),
                             join(base_dir, 'clean1_label.csv'))

    with open(join(module_path, 'descr', 'clean1.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target
    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=[])


def load_isolet(return_X_y=False):
    """Load and return the isolet dataset (classification).

    The spambase dataset is a classic and very easy multi-class classification
    dataset.

    =================   =================
    Classes                             2
    Samples per            class[300,300]
    Samples total                     600
    Dimensionality                     50
    Features             class_0, class_1
    =================   =================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=True.
        If True, returns ``(data, target)`` .
        See below for more information about the `data` and `target` object.

    Returns
    -------
    (data, target) : tuple if ``return_X_y`` is True
    """
    module_path = dirname(__file__)
    base_dir = join(module_path, 'data', 'isolet')
    data, target = load_data(join(base_dir, 'isolet_feature.csv'),
                             join(base_dir, 'isolet_label.csv'))

    with open(join(module_path, 'descr', 'isolet.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target
    
    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=[])
