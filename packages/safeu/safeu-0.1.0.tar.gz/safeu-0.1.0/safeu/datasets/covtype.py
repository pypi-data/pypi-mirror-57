"""covtype dataset.

The dataset page is available from UCI

    http://archive.ics.uci.edu/ml/datasets/Covertype

And the dataset with pretreatment can be found from

    http://lamda.nju.edu.cn/liangdm/data/covtype.tar.gz

"""
import os
import logging
import tarfile
import pickle
import codecs
from collections import namedtuple
from sklearn.utils import Bunch

import shutil
from os.path import dirname, join

logger = logging.getLogger(__name__)


RemoteFileMetadata = namedtuple('RemoteFileMetadata',
                                ['filename', 'url', 'checksum'])

ARCHIVE = RemoteFileMetadata(
    filename='covtype.tar.gz',
    url='http://lamda.nju.edu.cn/liangdm/data/covtype.tar.gz',
    checksum=('766d8160bcbabcc885e303253e3a5418218d789a9bfd06'
              'f081fd8d3a8f234cc9'))

CACHE_NAME = "covtype.pkz"

__all__ = ['load_covtype',
           'load_graph_covtype']


def download_covtype(target_dir, cache_path):
    """Download covtype dataset from website."""
    from .base import _fetch_remote

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    logger.info("Downloading dataset from %s ( MB)", ARCHIVE.url)

    archive_path = _fetch_remote(ARCHIVE, dirname=target_dir)
    print("Decompressing ", archive_path)

    tarfile.open(archive_path, "r").extractall(path=target_dir)
    os.remove(archive_path)

    cache = dict(covtype_X_y=_load_covtype(target_dir, False),
                 covtype_W=_load_graph_covtype(target_dir, False))
    compressed_content = codecs.encode(pickle.dumps(cache), 'zlib_codec')
    with open(cache_path, 'wb') as f:
        f.write(compressed_content)

    shutil.rmtree(target_dir)
    return cache


def fetch_covtype(data_home=None, subset=None,
               download_if_missing=True):

    from .base import get_data_home

    if data_home is None:
        data_home = join(dirname(__file__), 'data')

    data_home = get_data_home(data_home=data_home)
    cache_path = join(data_home, CACHE_NAME)

    covtype_home = os.path.join(data_home, "covtype_home")

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
            logger.info("Downloading covtype dataset. "
                        "This may take a few minutes.")
            cache = download_covtype(
                target_dir=covtype_home, cache_path=cache_path)
        else:
            raise IOError('covtype dataset not found')

    return cache[subset]


def load_covtype(return_X_y=False, data_home=None,
               download_if_missing=True):
    """Load and return the covtype dataset (classification).

    The covtype dataset is a classic and very easy multi-class classification
    dataset.

    =================   =====================
    Classes                                 2
    Samples per          class[297711,283301]
    Samples total                      581012
    Dimensionality                         54
    Features                class_1, class_-1
    =================   =====================

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

    bunch = fetch_covtype(data_home, 'covtype_X_y', download_if_missing)

    if return_X_y:
        return bunch.data, bunch.target

    return bunch


def load_graph_covtype(return_X_y=False, data_home=None,
                 download_if_missing=True):
    """Load and return sparse matrix of the covtype dataset (classification).

    The covtype dataset is a classic and very easy multi-class classification
    dataset.

    =================   =====================
    Classes                                 2
    Samples per          class[297711,283301]
    Samples total                      581012
    Dimensionality                         54
    Features                class_1, class_-1
    =================   =====================

    Read more in the :ref:`User Guide <datasets>`.

    Parameters
    ----------
    return_X_y : boolean, default=True.
        If True, returns ``(data, target)`` .
        See below for more information about the `data` and `target` object.

    Returns
    -------
    (data) : tuple if ``return_X_y`` is True
    """

    bunch = fetch_covtype(data_home, 'covtype_W', download_if_missing)

    if return_X_y:
        return bunch.data

    return bunch


def _load_covtype(target_dir=None, return_X_y=False):

    from .base import load_data

    module_path = dirname(__file__)
    if target_dir is None:
        target_dir = join(module_path, 'data', 'covtype')

    data, target = load_data(join(target_dir, 'covtype_feature.npz'),
                             join(target_dir, 'covtype_label.csv'))

    with open(join(module_path, 'descr', 'covtype.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=[])


def _load_graph_covtype(target_dir=None, return_X_y=False):

    from .base import load_graph_diff_formats

    module_path = dirname(__file__)
    if target_dir is None:
        target_dir = join(module_path, 'data', 'covtype')

    W = load_graph_diff_formats(join(target_dir, 'covtype_W.npz'))

    with open(join(module_path, 'descr', 'covtype.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return W

    return Bunch(data=W, target=None, DESCR=fdescr,
                 feature_names=[])
