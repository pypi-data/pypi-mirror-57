import numpy as np
import numpy.matlib as mat


def harmonic(W, y, l_ind, comp, baseline_pred):

    n_comp = comp.n
    ind_comp = comp.ind
    pred = np.zeros(np.size(W, 1), 1)
    pred_cmn = np.zeros(np.size(pred))
    for n in range(0, n_comp):
        ind = ind_comp(n)
        l_ind_comp = set(l_ind).intersection(ind)
        if not l_ind_comp:
            pred[ind] = baseline_pred[ind]
            pred_cmn[ind] = baseline_pred[ind]
        else:
            new_ind = np.zeros(1, len(l_ind_comp))
            for s in range(0, len(l_ind_comp)):
                new_ind[s] = np.where(ind == l_ind_comp[s])
            pred[ind], pred_cmn[ind] = sub_problem(W[ind, ind], y[ind], new_ind)


def sub_problem(W, y, l_ind):

    N = np.size(W, 1)
    u_ind = np.linspace(0, N - 1, N)
    u_ind = np.delete(u_ind, l_ind)
    ind = np.hstack((l_ind, u_ind))
    W = W[ind, ind]

    Y = np.zeros(l_ind, 2)
    y2 = np.array([-1, 1])
    for i in range(0, l_ind):
        for j in range(0, 2):
            Y[i, j] = (y[i] == y2[j])

    fu, fu_cmn = harmonic_function(W, Y)

    pred = np.zeros(N, 1)
    pred[l_ind] = y(l_ind)
    pred[u_ind] = fu[:, 1] - fu[:, 2]

    pred_cmn = pred
    pred_cmn[u_ind] = fu_cmn[:, 1] - fu_cmn[:, 2]

    return pred, pred_cmn


def harmonic_function(W, fl):
    col = np.size(fl, 1)
    n = np.size(W, 1)
    L = np.diag(np.sum(W, 2)) - W

    fu = -np.dot(L[col:n, col:n].I, np.dot(L[col:n, 0:col], fl))

    if any(sum(fu) == 0):
        fu_cmn = fu
    else:
        q = sum(fl) + 1
        fu_cmn = fu * mat.repmat(q / sum(fu), n - col, 1)

    return fu, fu_cmn
