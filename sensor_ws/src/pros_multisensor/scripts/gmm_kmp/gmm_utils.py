import numpy as np
from sklearn.mixture import BayesianGaussianMixture
from gmr import GMM, kmeansplusplus_initialization, covariance_initialization
from gmr.utils import check_random_state
import matplotlib.pyplot as plt

def generate_X_train(train_data_without_dx):
    """
    :param train_data_without_dx:
    train_data_without_dx[:,:,0] is phase 0-100
    train_data_without_dx[:,:,1:] is data
    :return:X_train
    with additional dx dimension
    """
    n_gait = np.shape(train_data_without_dx)[0]
    n_sample = np.shape(train_data_without_dx)[1]
    n_dim = np.shape(train_data_without_dx)[2] - 1
    X_train = np.zeros((n_gait, n_sample, 1 + n_dim * 2))
    X_train[:, :, 0:1 + n_dim] = train_data_without_dx
    dt = train_data_without_dx[0, 1, 0] - train_data_without_dx[0, 0, 0]
    for idx_gait in range(n_gait):
        for k in range(n_dim):
            X_train[idx_gait, :, 1 + n_dim + k] = np.gradient(X_train[idx_gait, :, 1 + k]) / dt
    X_train = X_train.reshape((-1, 1 + 2 * n_dim))
    return X_train


def train_GMM(X_train, n_components):
    random_state = check_random_state(0)
    initial_means = kmeansplusplus_initialization(X_train, n_components, random_state)
    initial_covs = covariance_initialization(X_train, n_components)
    bgmm = BayesianGaussianMixture(n_components=n_components, max_iter=400).fit(X_train)
    gmm = GMM(n_components=n_components,
              priors=bgmm.weights_,
              means=bgmm.means_,
              covariances=bgmm.covariances_,
              random_state=random_state)
    return gmm


def gmm_Interp_with_phase(gmm, phase):
    """
    :param gmm:
    :param phase: phase should be 0-100  (len,)
    :return:
    """
    mean_list = []
    sigma_list = []
    for i in range(np.shape(phase)[0]):
        phase_i = phase[i]
        conditional_gmm = gmm.condition([0], np.array([phase_i]))
        condition_mvn = conditional_gmm.to_mvn()
        mean_list.append(condition_mvn.mean)
        sigma_list.append(condition_mvn.covariance)
        # samples = conditional_gmm.sample(100)
        # plt.scatter(samples[:, 0], samples[:, 1], s=1)
    mean_list = np.array(mean_list)
    sigma_list = np.array(sigma_list)
    return mean_list, sigma_list
