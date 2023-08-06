"""usps dataset.

Handwritten recognition for digital acquisition. There are a total of 9298
handwritten digital images in the library(both 16*16 pixel grayscale values,
the grayscale values have been normalized).And the dataset is divided into train
and test.

The dataset page is available from LIBSVM

    https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass.html#usps

And the dataset with pretreatment can be found from

    http://lamda.nju.edu.cn/liangdm/data/usps.tar.gz

"""

import os
import logging
import tarfile
import pickle
import codecs
from collections import namedtuple

import numpy as np
from sklearn.utils import Bunch

import shutil
from os.path import dirname, join

logger = logging.getLogger(__name__)


RemoteFileMetadata = namedtuple('RemoteFileMetadata',
                                ['filename', 'url', 'checksum'])

ARCHIVE = RemoteFileMetadata(
    filename='usps.tar.gz',
    url='http://lamda.nju.edu.cn/liangdm/data/usps.tar.gz',
    checksum=('22aec85cb31775b4fb3bbed9f16220c4e00c2bc'
              '259cc21282f26bb76c9aad03e'))

CACHE_NAME = "usps.pkz"

__all__ = ['load_usps']


def download_usps(target_dir, cache_path):
    """Download usps dataset from website."""
    from .base import _fetch_remote

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    logger.info("Downloading dataset from %s ( MB)", ARCHIVE.url)

    archive_path = _fetch_remote(ARCHIVE, dirname=target_dir)
    print("Decompressing ", archive_path)

    tarfile.open(archive_path, "r").extractall(path=target_dir)
    os.remove(archive_path)

    cache = dict(train=load_usps_train(target_dir, False),
                 test=load_usps_test(target_dir, False))
    compressed_content = codecs.encode(pickle.dumps(cache), 'zlib_codec')
    with open(cache_path, 'wb') as f:
        f.write(compressed_content)

    shutil.rmtree(target_dir)
    return cache


def load_usps(data_home=None, subset='train',
               download_if_missing=True,
               return_X_y=False):
    """Load the filenames and data from the usps dataset.

    Parameters
    ----------
    data_home : optional, default: None
        Specify a download and cache folder for the datasets.

    subset : 'train' or 'test', optional
        Select the dataset to load: 'train' for the training set, 'test'
        for the test set.

    download_if_missing : optional, default: True
        If False, raise an IOError if the data is not locally available
        instead of trying to download the data from the source site.

    return_X_y:optional,default: false
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
    """
    from .base import get_data_home

    if data_home is None:
        data_home = join(dirname(__file__), 'data')

    data_home = get_data_home(data_home=data_home)
    cache_path = join(data_home, CACHE_NAME)

    usps_home = os.path.join(data_home, "usps_home")

    cache = None
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'rb') as f:
                compressed_content = f.read()
            uncompressed_content = codecs.decode(
                compressed_content, 'zlib_codec')
            cache = pickle.loads(uncompressed_content)
        except Exception as e:
            print(80 * '_' + 'Cache loading failed' + 80 * '_' + e)

    if cache is None:
        if download_if_missing:
            logger.info("Downloading usps dataset. "
                        "This may take a few minutes.")
            cache = download_usps(target_dir=usps_home, cache_path=cache_path)
        else:
            raise IOError('usps dataset not found')

    if subset in ('train', 'test'):
        bunch = cache[subset]
    else:
        raise ValueError(
            "subset can only be 'train', 'test' or 'all', got '%s'" % subset)
    if return_X_y:
        return bunch.data, bunch.target

    return bunch


def load_usps_train(target_dir, return_X_y=False):
    """
    load usps database.
    """
    module_path = dirname(__file__)
    data = np.loadtxt(join(target_dir, 'usps_feature.csv'))
    target = np.loadtxt(join(target_dir, 'usps_target.csv'))
    target = np.reshape(target, (data.shape[0], 1)).astype(int)

    with open(join(module_path, 'descr', 'usps.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=[])


def load_usps_test(target_dir, return_X_y=False):
    """
    load usps_test database.
    """
    module_path = dirname(__file__)
    data = np.loadtxt(join(target_dir, 'usps_test_feature.csv'))
    target = np.loadtxt(join(target_dir, 'usps_test_target.csv'))
    target = np.reshape(target, (data.shape[0], 1)).astype(int)

    with open(join(module_path, 'descr', 'usps.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=[])
