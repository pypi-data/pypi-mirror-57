# -*- coding: utf-8 -*-

"""
This file implements some useful functions used to manipulate the data
features or labels.
"""
import os

import numpy as np
import scipy.sparse as sp
from sklearn.utils.validation import check_array
from sklearn.model_selection import RepeatedKFold

# Data Split
"""
Data Split: Split the original dataset into train/test label/unlabel set.
"""

__all__ = ['inductive_split', 'ratio_split',
    'cv_split', 'split_load', 'check_y', 'check_inputs', 'modify_y']


def inductive_split(X=None, y=None, instance_indexes=None, test_ratio=0.3,
                    initial_label_rate=0.05, split_count=10, all_class=True,
                    save_file=False, saving_path=None, name=None):
    """Provided one of X, y or instance_indexes to execute the inductive split.
    
    Return the indexs for train/test data, and labled/unlabeled data in train
    ones for each split. If X, y are both provided, the lengths 
    of them should be the same.

    Parameters
    ----------
    X : array-like, optional
        Data matrix with [n_instances, n_features]

    y : array-like, optional
        labels of given data [n_instances, n_labels] or [n_instances]

    instance_indexes: list, optional (default=None)
        List contains instances' names, used for image datasets,
        or provide index list instead of data matrix.
        Must provide one of [instance_names, X, y]

    test_ratio : float, optional (default=0.3)
        Ratio of test set

    initial_label_rate : float, optional (default=0.05)
        Ratio of initial label set
        e.g. Initial_labelset*(1-test_ratio)*n_instances

    split_count : int, optional (default=10)
        Random split data _split_count times

    all_class: bool, optional (default=True)
        Whether each split will contain at least one instance for each class.
        If False, a totally random split will be performed.

    save_file : boolean, optional (default=False)

    saving_path : str, optional (default='.')
        Giving None to disable saving.

    name : str, optional (default=None)
        Dataset name.

    Returns
    -------
    train_idx : list
        index of training set, shape like [n_split_count, n_training_indexes]
    test_idx : list
        index of testing set, shape like [n_split_count, n_testing_indexes]
    label_idx : list
        index of labeling set, shape like [n_split_count, n_labeling_indexes]
    unlabel_idx : list
        index of unlabeling set, shape like [n_split_count,
        n_unlabeling_indexes]
    """

    # check parameters
    if X is None and y is None and instance_indexes is None:
        raise ValueError("Must provide one of X, y or instance_indexes.")

    if isinstance(X, sp.spmatrix):
        len_of_parameters = [X.shape[0] if X is not None else None,
                             len(y) if y is not None else None]
    else:
        len_of_parameters = [len(X) if X is not None else None,
                             len(y) if y is not None else None]

    number_of_instance = np.unique(
        [i for i in len_of_parameters if i is not None])
    if len(number_of_instance) > 1:
        raise ValueError("Different length of instances and _labels found.")
    elif len(number_of_instance) == 0:  # only instance_indexes
        number_of_instance = len(instance_indexes)
    else:
        number_of_instance = number_of_instance[0]

    if instance_indexes is not None:
        if not isinstance(instance_indexes, (list, np.ndarray)):
            raise TypeError("A list or np.ndarray object is expected, "
                            "but received: %s" % str(type(instance_indexes)))
        instance_indexes = np.array(instance_indexes)
        if y is not None and max(instance_indexes) >= len(y):
            raise ValueError("Instance index out of range")
    else:
        instance_indexes = np.arange(number_of_instance)

    # split
    train_idx = []
    test_idx = []
    label_idx = []
    unlabel_idx = []
    for i in range(split_count):
        if (not all_class) or (y is not None and isinstance(y[0], float)):
            rp = _randperm(number_of_instance - 1)
            cutpoint = int(round((1 - test_ratio) * len(rp)))
            tp_train = instance_indexes[rp[0:cutpoint]]
            train_idx.append(tp_train)
            test_idx.append(instance_indexes[rp[cutpoint:]])
            cutpoint = int(round(initial_label_rate * len(tp_train)))
            if cutpoint <= 1:
                cutpoint = 1
            label_idx.append(tp_train[0:cutpoint])
            unlabel_idx.append(tp_train[cutpoint:])
        else:
            if y is None:
                raise ValueError(
                    "y must be provided when all_class flag is True.")
            y = check_array(y, ensure_2d=False, dtype=None)
            if y.ndim == 1:
                label_num = len(np.unique(y))
            else:
                label_num = y.shape[1]
            if round((1 - test_ratio) * initial_label_rate
                             * number_of_instance) < label_num:
                raise ValueError(
                    "The initial rate is too small to guarantee that each "
                    "split will contain at least one instance for each class.")

            # check validaty
            while 1:
                rp = _randperm(number_of_instance - 1)
                cutpoint = int(round((1 - test_ratio) * len(rp)))
                tp_train = instance_indexes[rp[0:cutpoint]]
                cutpointlabel = int(round(initial_label_rate * len(tp_train)))
                if cutpointlabel <= 1:
                    cutpointlabel = 1
                label_id = tp_train[0:cutpointlabel]
                if y.ndim == 1:
                    if len(np.unique(y[label_id])) == label_num:
                        break
                else:
                    temp = np.sum(y[label_id], axis=0)
                    if not np.any(temp == 0):
                        break
            train_idx.append(tp_train)
            test_idx.append(instance_indexes[rp[cutpoint:]])
            label_idx.append(tp_train[0:cutpointlabel])
            unlabel_idx.append(tp_train[cutpointlabel:])

    if save_file:
        _split_save(train_idx=train_idx, test_idx=test_idx, label_idx=label_idx,
                    unlabel_idx=unlabel_idx, path=saving_path, name=name)
    return train_idx, test_idx, label_idx, unlabel_idx


def ratio_split(X=None, y=None, instance_indexes=None, unlabel_ratio=0.3,
                split_count=10, all_class=True, save_file=False,
                saving_path=None, name=None):
    """Split the data into labeled and unlabeled set with given ratio.

    Provide one of X, y or instance_indexes to execute the transductive split. 
    If X, y are both provided, the lengths of them should be the same. If X,
    instance_indexes are both provided, the instance_indexes is used for split.

    Parameters
    ----------
    X : array-like, optional
        Data matrix with [n_instances, n_features]

    y : array-like, optional
        labels of given data [n_instances, n_labels] or [n_instances]

    instance_indexes : list, optional (default=None)
        List contains instances' names, used for image datasets,
        or provide index list instead of data matrix.
        Must provide one of [instance_names, X, y]

    unlabel_ratio : float, optional (default=0.3)
        Ratio of test set

    split_count : int, optional (default=10)
        Random split data _split_count times

    all_class : bool, optional (default=True)
        Whether each split will contain at least one instance for each class.
        If False, a totally random split will be performed.

    save_file : boolean, optional (default=False)

    saving_path : str, optional (default='.')
        Giving None to disable saving.

    name : str, optional (default=None)
        Dataset name.

    Returns
    -------
    train_idxs : list
        index of training set, shape like [n_split_count, n_training_indexes]

    test_idxs : list
        index of testing set, shape like [n_split_count, n_testing_indexes]
    """

    # check parameters
    if X is None and y is None and instance_indexes is None:
        raise ValueError("Must provide one of X, y or instance_indexes.")

    if isinstance(X, sp.spmatrix):
        len_of_parameters = [X.shape[0] if X is not None else None,
                             len(y) if y is not None else None]
    else:
        len_of_parameters = [len(X) if X is not None else None,
                             len(y) if y is not None else None]

    number_of_instance = np.unique(
        [i for i in len_of_parameters if i is not None])
    
    if len(number_of_instance) > 1:
        raise ValueError("Different length of instances and _labels found.")
    elif len(number_of_instance) == 0:
        number_of_instance = len(instance_indexes)
    else:
        number_of_instance = number_of_instance[0]

    if instance_indexes is not None:
        if not isinstance(instance_indexes, (list, np.ndarray)):
            raise TypeError("A list or np.ndarray object is expected,"
                            " but received: %s" % str(type(instance_indexes)))
        instance_indexes = np.array(instance_indexes)
        if y is not None and max(instance_indexes) >= len(y):
            raise ValueError("Instance index out of range")
    else:
        instance_indexes = np.arange(number_of_instance)

    # split
    train_idxs = []
    test_idxs = []
    for i in range(split_count):
        if (not all_class) or (y is not None and isinstance(y[0], float)):
            rp = _randperm(number_of_instance - 1)
            cutpoint = int(round((1 - unlabel_ratio) * len(rp)))
            tp_train = instance_indexes[rp[0:cutpoint]]
            train_idxs.append(tp_train)
            test_idxs.append(instance_indexes[rp[cutpoint:]])
            '''cutpoint = int(round(initial_label_rate * len(tp_train)))
            if cutpoint <= 1:
                cutpoint = 1'''
        else:
            if y is None:
                raise ValueError(
                    "y must be provided when all_class flag is True.")
            y = check_array(y, ensure_2d=False, dtype=None)
            if y.ndim == 1:
                label_num = len(np.unique(y))
            else:
                label_num = y.shape[1]
            if round((1 - unlabel_ratio) * number_of_instance) < label_num:
                raise ValueError(
                    "The label rate is too small to guarantee that each "
                    "split will contain at least one instance for each class.")

            # check validaty
            while 1:
                rp = _randperm(number_of_instance - 1)
                cutpoint = int(round((1 - unlabel_ratio) * len(rp)))
                tp_train = instance_indexes[rp[0:cutpoint]]

                # cutpointlabel = int(round(initial_label_rate * len(tp_train)))
                if cutpoint <= 1:
                    cutpoint = 1
                label_id = tp_train[0:cutpoint]
                if y.ndim == 1:
                    if len(np.unique(y[label_id])) == label_num:
                        break
                else:
                    temp = np.sum(y[label_id], axis=0)
                    if not np.any(temp == 0):
                        break
            train_idxs.append(tp_train)
            test_idxs.append(instance_indexes[rp[cutpoint:]])

    if save_file:
        _split_save(train_idx=train_idxs, test_idx=test_idxs,
                    path=saving_path, name=name)
    return train_idxs, test_idxs


def cv_split(X=None, y=None, instance_indexes=None, k=3, split_count=10,
             all_class=True, save_file=False, saving_path=None, name=None):
    """Split the data into labeled and unlabeled set with given ratio.

    Provide one of X, y or instance_indexes to execute the transductive split.
    Use instance_indexes firstly.

    Note
    ---- 
    1. For multi-label task, set all_class = False.
    2. For classification, the label must not be float type

    Parameters
    ----------
    X : array-like, optional
        Data matrix with [n_instances, n_features]

    y : array-like, optional
        labels of given data [n_instances, n_labels] or [n_instances]

    instance_indexes : list, optional (default=None)
        List provides index list instead of X.
        Must provide one of [instance_names, X, y]

    k : int, optional (default=3)
        Parameter for k-fold split. k should be small enough when we have
        few label data.

    split_count : int, optional (default=10)
        Random split data _split_count times

    all_class : bool, optional (default=True)
        Whether each split will contain at least one instance for each class.
        If False, a totally random split will be performed.

    save_file : boolean, optional (default=False)
        A flag indicates whether to save the splits.

    saving_path : str, optional (default='.')
        Giving None to disable saving.

    name : str, optional (default=None)
        Dataset name.

    Returns
    -------
    train_idx : list
        index of training set, shape like [n_split_count, n_training_indexes]

    test_idx : list
        index of testing set, shape like [n_split_count, n_testing_indexes]
    """

    # check parameters
    if X is None and y is None and instance_indexes is None:
        raise ValueError("Must provide one of X, y or instance_indexes.")

    if isinstance(X, sp.spmatrix):
        len_of_parameters = [X.shape[0] if X is not None else None,
                             len(y) if y is not None else None]
    else:
        len_of_parameters = [len(X) if X is not None else None,
                             len(y) if y is not None else None]

    number_of_instance = np.unique(
        [i for i in len_of_parameters if i is not None])
    if len(number_of_instance) > 1:
        raise ValueError("Different length of instances X and _labels Y found.")
    else:
        number_of_instance = number_of_instance[0]

    # organize instance_indexes
    if instance_indexes is not None:
        if not isinstance(instance_indexes, (list, np.ndarray)):
            raise TypeError("A list or np.ndarray object is expected, "
                            "but received: %s" % str(type(instance_indexes)))
        instance_indexes = np.array(instance_indexes)
    else:
        instance_indexes = np.arange(number_of_instance)

    rkf = RepeatedKFold(n_splits=k, n_repeats=split_count)
    train_idxs = []
    test_idxs = []

    # rkf.split based on len(input)
    # totally random k-fold split
    if (not all_class) or (y is not None and ((y.ndim == 1
            and isinstance(y[0], float)) or (y.ndim == 2 
            and y.shape[1] == 1 and isinstance(y[0][0], float)))):
        # not all_class, multi-label or regression
        for train_idx, test_idx in rkf.split(instance_indexes):
            train_idxs.append(instance_indexes[train_idx])
            test_idxs.append(instance_indexes[test_idx])

    else:
        for i in range(split_count * k):
            train_idxs.append([])
            test_idxs.append([])

        if y is None:
            raise ValueError("y must be provided when all_class flag is True.")
        
        # if y.ndim != 2:
        #     raise ValueError("The shape of y must be 2-d.")

        if y.ndim == 1 or y.shape[1] == 1:  # y is the label vector
            labels = np.unique(y)
            for label in labels:
                group_index = [
                    idx for idx in instance_indexes if y[idx] == label]
                if len(group_index) < k:
                    raise ValueError("The k is too large to guarantee that "
                                     "each split will contain at least one "
                                     "instance for each class.")
                i = 0
                for train_idx, test_idx in rkf.split(group_index):
                    train_idxs[i] = [] + train_idxs[i] + \
                        [group_index[i] for i in train_idx]
                    test_idxs[i] = [] + test_idxs[i] + [group_index[i]
                        for i in test_idx]
                    i += 1
        else:  # y is the proba matrix, only for multi-class
            y_check = np.all(np.sum(y, axis=1) == 1)
            if not y_check:
                raise ValueError("Each instance belongs to one class!")
            
            label_num = y.shape[1]
            labels = np.arange(label_num)
            for label in labels:
                group_index = [
                    idx for idx in instance_indexes if y[idx, label] > 0]
                if len(group_index) < k:
                    raise ValueError("The k is too large to guarantee that "
                                     "each split will contain at least one "
                                     "instance for each class.")
                i = 0
                for train_idx, test_idx in rkf.split(group_index):
                    train_idxs[i] = [] + train_idxs[i] + \
                        [group_index[i] for i in train_idx]
                    test_idxs[i] = [] + test_idxs[i] + [group_index[i]
                        for i in test_idx]
                    i += 1
        for i in range(split_count * k):
            train_idxs[i] = np.array(train_idxs[i])
            test_idxs[i] = np.array(test_idxs[i])
    if save_file:
        _split_save(train_idx=train_idxs, test_idx=test_idxs,
                    path=saving_path, name=name)
    return train_idxs, test_idxs


def _split_save(train_idx, test_idx, path, name, label_idx=None,
                unlabel_idx=None):
    """Save the split to file for auditting or loading for other methods.

    Parameters
    ----------
    saving_path : str
        path to save the settings. If a dir is not provided, it will generate
         a folder called 'alipy_split' for saving.

    """
    if path is None:
        raise Exception("A path to a directory is expected.")
    else:
        if not isinstance(path, str):
            raise TypeError(
                "A string is expected, but received: %s" % str(type(path)))

    saving_path = os.path.abspath(path)
    if os.path.isdir(saving_path):
        if not os.path.exists(os.path.join(saving_path, name)):
            os.mkdir(os.path.join(saving_path, name))
        np.savetxt(os.path.join(saving_path, name,
                   '_train_idx.txt'), train_idx, fmt='%d')
        np.savetxt(os.path.join(saving_path, name,
                   '_test_idx.txt'), test_idx, fmt='%d')
        if label_idx and unlabel_idx:
            if len(np.shape(label_idx)) == 2:
                np.savetxt(os.path.join(saving_path, name,
                           '_label_idx.txt'), label_idx, fmt='%d')
                np.savetxt(os.path.join(saving_path, name,
                           '_unlabel_idx.txt'), unlabel_idx, fmt='%d')
            else:
                np.save(os.path.join(saving_path, name,
                        '_label_idx.npy'), label_idx)
                np.save(os.path.join(saving_path, name,
                        '_unlabel_idx.npy'), unlabel_idx)
    else:
        raise Exception("A path to a directory is expected.")


def split_load(path, name):
    """Load split from path.

    Parameters
    ----------
    path : str
        Absolute path to a dir which contains train_idx.txt, test_idx.txt,
        label_idx.txt, unlabel_idx.txt.

    name : str
        The name of dataset. The file is stored as 'XXX_train/test_idx.txt/npy'
    
    Returns
    -------
    train_idx : list
        index of training set, shape like [n_split_count, n_training_samples]

    test_idx : list
        index of testing set, shape like [n_split_count, n_testing_samples]

    label_idx : list
        index of labeling set, shape like [n_split_count, n_labeling_samples]

    unlabel_idx : list
        index of unlabeling set, shape like
        [n_split_count, n_unlabeling_samples]
    """
    if not isinstance(path, str):
        raise TypeError("A string is expected, but received: %s" %
                        str(type(path)))
    saving_path = os.path.abspath(path)
    if not os.path.isdir(saving_path):
        raise Exception("A path to a directory is expected.")

    ret_arr = []
    for fname in ['_train_idx.txt', '_test_idx.txt', '_label_idx.txt',
                  '_unlabel_idx.txt']:
        if not os.path.exists(os.path.join(saving_path, name, fname)):
            if os.path.exists(os.path.join(saving_path, name,
                                           fname.split()[0] + '.npy')):
                ret_arr.append(np.load(os.path.join(
                    saving_path, name, fname.split()[0] + '.npy')))
            else:
                ret_arr.append(None)
        else:
            ret_arr.append(np.loadtxt(os.path.join(
                saving_path, name, fname), dtype=int))
    return ret_arr[0], ret_arr[1], ret_arr[2], ret_arr[3]


def _randperm(n, k=None):
    """Generate a random array which contains k elements range from (n[0]:n[1])

    Parameters
    ----------
    n : int or tuple
        range from [n[0]:n[1]], include n[0] and n[1].
        if an int is given, then n[0] = 0

    k : int, optional (default=end - start + 1)
        how many numbers will be generated. should not larger than n[1]-n[0]+1,
        default=n[1] - n[0] + 1.

    Returns
    -------
    perm : list
        the generated array.
    """
    if isinstance(n, np.generic):
        # n = np.asscalar(n)
        n = n.item()
    if isinstance(n, tuple):
        if n[0] is not None:
            start = n[0]
        else:
            start = 0
        end = n[1]
    elif isinstance(n, int):
        start = 0
        end = n
    else:
        raise TypeError("n must be tuple or int.")

    if k is None:
        k = end - start + 1
    if not isinstance(k, int):
        raise TypeError("k must be an int.")
    if k > end - start + 1:
        raise ValueError("k should not larger than n[1]-n[0]+1")

    randarr = np.arange(start, end + 1)
    np.random.shuffle(randarr)
    return randarr[0:k]


def check_inputs(X, y, binary=True):
    """
    Transform the input label vector to proba matrix; 
    Encode the str feature.

    Parameters
    ----------
    X : np.ndarray
        Features
    
    y : np.ndarray
        Labels
    """
    labels, y_t = check_y(y, binary)
    if type(X[0][0]) is str:
        _, X_t = check_y(X, binary)
    else:
        X_t = X
    return X_t, y_t, labels


def check_y(y, binary=True):
    """ 
    Transform label vector to proba matrix. Use for binary and multi-class
    tasks.

    Parameters
    ----------
    y : np.ndarray
        Original label vector.
    binary: boolean (default=True)
        Indicate different tasks.
    
    Return
    ------
    labels : 1-D np.ndarray
        A vector store the original labels. The labels are sorted as in `y_t`.
    y_t : np.ndarray
        When binary == True, y_t is 1-D vector with {1,-1}.
        When binary == False, y_t is a matrix in the shape n_samples, n_classes.
    """
    if binary:
        labels = np.unique(y)
        y_t = np.zeros_like(y)
        if len(labels) > 2:
            raise Exception(
                "y is a two-category data tag should have only two values.")

        y_t[y == labels[0]] = -1
        y_t[y == labels[1]] = 1
        return labels, y_t
    else:
        labels = np.unique(y)
        y_t = np.zeros([y.shape[0], len(labels)])
        for i, label in enumerate(labels):
           for j in range(0, len(y)):
               if y[j] == label:
                    y_t[j, i] = 1
        return labels, y_t


def modify_y(y, ind, n_labels, binary=True):
    """
    This function is the reverse function of `check_y`, which transfer the 
    prediction from inner results to the origin labels.

    Parameters
    ----------
    y : np.ndarray
        Prediction
    
    ind : np.ndarray
        Index
    
    n_labels : 1-D np.ndarray
        A vector store the original labels. The labels are sorted as in `y`.

    """
    type_ = type(n_labels[0])
    res = np.empty((len(ind), y.shape[1]), dtype=type_)

    if binary:
        res[y[ind] == -1] = n_labels[0]
        res[y[ind] == 1] = n_labels[1]
    return res
