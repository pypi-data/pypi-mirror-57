import numpy as np
from scipy import sparse


def construct_graph(dis, k):
    """

    :param dis: distance matrix
    :param k: number of nearest neighborhoods
    :return W: graph matrix
    """

    N = np.size(dis, 1)
    dis = dis + (np.zeros((N, N)) + float('inf'))
    weight = np.zeros(N)
    for i in range(0, N):
        ind = np.argsort(-dis[i, :])
        weight[i, ind[0:k]] = 1
    W = sparse.dok_matrix(weight | weight.T)

    return W
