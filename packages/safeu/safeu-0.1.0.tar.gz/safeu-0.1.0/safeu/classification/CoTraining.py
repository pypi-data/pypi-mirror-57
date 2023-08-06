from sklearn.svm import SVC
import numpy as np
from ..base import InductiveEstimatorWOGraph
from ..datasets.data_manipulate import check_y, modify_y


class CoTraining(InductiveEstimatorWOGraph):
    """CoTraining classifier

    Parameters
    ----------

    pos: int (default=1)
        The number of positive samples selected in each contraining iteration

    neg: int (default=1)
        The number of negative samples selected in each contraining iteration

    model: object
        [model1,model2] initializing model1 for view1 and model2 for view2

    ind1: array-like [] (default=0)
        The column index of view1 in features X

    ind2: array-like [] (default=0)
        The column index of view2 in features X

    nepo: int (default=40)
        The number of iteration

    buffer_size: int (default=200)
        The size of buffer

    Attributes
    ----------
    model: object list
        Two best model for view1 and view2.
    """

    def __init__(self, pos=1, neg=1,
                 model1=SVC(probability=True, gamma="auto"),
                 model2=SVC(probability=True, gamma="auto"),
                 ind1=np.arange(0),
                 ind2=np.arange(0),
                 nepo=40,
                 buffer_size=200):
        super(CoTraining, self).__init__()
        self.pos = pos
        self.neg = neg
        self.model = [model1, model2]
        self.ind1 = ind1
        self.ind2 = ind2
        self.nepo = nepo
        self.buffer_size = buffer_size

        self.n_labels = None

    def set_params(self, param):
        if isinstance(param, dict):
            self.__dict__.update(param)
        # self.pos = param.pop('pos', self.pos)
        # self.neg = param.pop('neg', self.neg)
        # self.model = param.pop('model', self.model)
        # self.ind1 = param.pop('ind1', self.ind1)
        # self.ind2 = param.pop('ind2', self.ind2)
        # self.nepo = param.pop('nepo', self.nepo)
        # self.buffer_size = param.pop('buffer_size', self.buffer_size)
        self.n_labels = None

    def fit(self, X, targets, labeled_idx):
        """Fit a cotraining model

        All the input data is provided matrix X (labeled and unlabeled)
        and corresponding label matrix y with a dedicated marker value for
        unlabeled samples.

        Parameters
        ----------
        feature1 : view1 array-like, shape = [n_samples, n_features]

        feature2 : view2 array_like, shape = [n_samples, n_features]

        targets : array_like, shape = [n_samples]
            label of n_labeled_samples in X.

        labeled_ind: the index of labeled data in targets.
        For example: [1,2,500,600]

        Returns
        -------
        self : returns an instance of self.
        """
        self.n_labels, targets_ = check_y(targets)
        feature1 = X[:, self.ind1]
        feature2 = X[:, self.ind2]
        self._fit(feature1, feature2, targets_.astype(np.int), labeled_idx)

    def _fit(self, feature1, feature2, targets, labeled_ind):  #
        targets[targets == -1] = 0

        train_ind = range(feature1.shape[0])

        self.model[0].fit(feature1[labeled_ind], targets[labeled_ind].ravel())

        self.model[1].fit(feature2[labeled_ind], targets[labeled_ind].ravel())

        unlabeled_ind = list(set(train_ind) - set(labeled_ind)) 

        # reading a buffer Ds
        if self.buffer_size > len(unlabeled_ind):
            npool = int(len(unlabeled_ind) * 0.7)
        else:
            npool = self.buffer_size

        un_pselabeled_ind_pool = np.array(
            (np.random.permutation(unlabeled_ind)[:npool]))

        rest = list(set(unlabeled_ind) - set(un_pselabeled_ind_pool))  # Du \ Ds

        all_pse_labeled_ind = []
        all_pse_label = []

        for epo in range(self.nepo):
            # the rest < self.pos+self.neg ,ending
            if len(un_pselabeled_ind_pool) < self.pos + self.neg:
                break

            pseudo_label1 = self.model[0].predict(
                feature1[un_pselabeled_ind_pool])
            prob1 = np.max(self.model[0].predict_proba(
                feature1[un_pselabeled_ind_pool]))

            pseudo_label2 = self.model[1].predict(
                feature2[un_pselabeled_ind_pool])
            prob2 = np.max(self.model[1].predict_proba(
                feature2[un_pselabeled_ind_pool]))

            sign_prob1 = prob1 * (2 * pseudo_label1 - 1)  # {0,1} -> {-1,1}
            sign_prob2 = prob2 * (2 * pseudo_label2 - 1)
            # If the prediction is 0, the probability is negative, so the
            # maximum probability of the positive and negative examples
            # correspond to the maximum and minimum values of sign_prob
            # respectively

            # append pseudo_label
            pse_labeled_ind = []
            pse_label = []
            pse_labeled_ind1 = []
            pse_label1 = []
            pse_labeled_ind2 = []
            pse_label2 = []

            # model1 and model2 give the high confident pse_label of unlabeled
            # samples respectively
            self.pos_avai1 = min(sum(pseudo_label1 == 1), self.pos)
            self.neg_avai1 = min(sum(pseudo_label1 == 0), self.neg)
            if self.pos_avai1 > 0:
                pse_labeled_ind1 += list(un_pselabeled_ind_pool[list(
                    reversed(np.argsort(sign_prob1)))[:self.pos_avai1]])
                # Convert to the original subscript
                pse_label1 += [1] * self.pos_avai1

            if self.neg_avai1 > 0:
                pse_labeled_ind1 += list(un_pselabeled_ind_pool[np.argsort(
                    sign_prob1)[:self.neg_avai1]])
                pse_label1 += [0] * self.neg_avai1
            # pse_labeled_ind1->the index of samples in view1,
            # pse_label1 -> the label of samples in view1

            self.pos_avai2 = min(sum(pseudo_label2 == 1), self.pos)
            self.neg_avai2 = min(sum(pseudo_label2 == 0), self.neg)
            # use reversed(A)[:self.pos] is better than A[-self.pos:],
            # even if  self.pos=0 ,it is still not wrong.
            if self.pos_avai2 > 0:
                pse_labeled_ind2 += list(un_pselabeled_ind_pool[list(
                    reversed(np.argsort(sign_prob2)))[:self.pos_avai2]])

                pse_label2 += [1] * self.pos_avai2
            if self.neg_avai2 > 0:
                pse_labeled_ind2 += list(un_pselabeled_ind_pool[np.argsort(
                    sign_prob2)[:self.neg_avai2]])

                pse_label2 += [0] * self.neg_avai2
            # pse_labeled_ind2->the index of samples in view2,
            # pse_label2 -> the label of samples in view2

            # handling the conflict
            # check coincidence
            if set(pse_labeled_ind1) & set(pse_labeled_ind2):
                for x in set(pse_labeled_ind1) - set(pse_labeled_ind2):
                    id1 = pse_labeled_ind1.index(x)
                    pse_labeled_ind.append(x)
                    pse_label.append(pse_label1[id1])

                for x in set(pse_labeled_ind2) - set(pse_labeled_ind1):
                    id2 = pse_labeled_ind2.index(x)
                    pse_labeled_ind.append(x)
                    pse_label.append(pse_label2[id2])

                for x in set(pse_labeled_ind1) & set(pse_labeled_ind2):
                    id1 = pse_labeled_ind1.index(x)
                    id2 = pse_labeled_ind2.index(x)
                    if pse_label1[id1] != pse_label2[id2]:  # conflict
                        pass
                    else:
                        pse_labeled_ind.append(x)
                        pse_label.append(pse_label1[id1])
            else:  # no codicidence
                pse_labeled_ind += pse_labeled_ind1
                pse_labeled_ind += pse_labeled_ind2
                pse_label += pse_label1
                pse_label += pse_label2
            # pse_labeled_ind->the index of pse_labeled samples
            # pse_label->the label of pse_labeled samples

            # update un_pseudo label pool and rest
            un_pselabeled_ind_pool = list(
                set(un_pselabeled_ind_pool) - set(pse_labeled_ind))

            append_pool = []
            if len(rest) > 0:
                if len(rest) >= 2 * (self.pos + self.neg):
                    append_pool = list(np.random.permutation(rest)[
                                       :2 * (self.pos + self.neg)])
                else:
                    append_pool = list(rest)

            un_pselabeled_ind_pool += append_pool  # expanding U‘
            un_pselabeled_ind_pool = np.array(un_pselabeled_ind_pool)
            rest = list(set(rest) - set(append_pool))

            # update pseudo label
            all_pse_labeled_ind += pse_labeled_ind
            all_pse_label += pse_label

            all_labeled = list(labeled_ind) + all_pse_labeled_ind

            assert len(all_pse_labeled_ind) == len(all_pse_label)

            all_target = np.array(
                list(targets[labeled_ind]) + all_pse_label, dtype=int)

            self.model[0].fit(feature1[all_labeled], all_target)
            self.model[1].fit(feature2[all_labeled], all_target)

    def predict(self, X, select_1=True):
        """
        Parameters
        ----------
        X: np.ndarray, shape = [n_samples, n_features]
            samples to be predicted

        select_1: boolean, optional
            select the prediction of model1 and model2.

        Returns
        -------
        y: np.ndarray, shape = [n_samples]
            Predictions for input data
        """
        if select_1:
            raw_pred = self.model[0].predict(X[:, self.ind1]).reshape(-1, 1)
            raw_pred[raw_pred == 0] = -1
            return modify_y(raw_pred, range(0, len(X)), self.n_labels)
        else:
            raw_pred = self.model[0].predict(X[:, self.ind2]).reshape(-1, 1)
            raw_pred[raw_pred == 0] = -1
            return modify_y(raw_pred, range(0, len(X)), self.n_labels)
