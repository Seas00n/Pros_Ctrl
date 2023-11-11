import numpy as np
import os
import glob
from gmr import GMM, kmeansplusplus_initialization, covariance_initialization
from gmr.utils import check_random_state
import matplotlib.pyplot as plt
from sklearn.mixture import BayesianGaussianMixture

save_path = "/media/yuxuan/My Passport/Open_Source_Data/gmm_data/"
fp_file_list = glob.glob(save_path+"*.npy")

train_data_list = []
for file in fp_file_list[0:40]:
    fp = np.load(file).T
    fp[:,0] = np.linspace(0,1,100)
    train_data_list.append(fp[:,(0,2,3)])

train_data = np.array(train_data_list)
plt.plot(train_data[:,:,0].T,train_data[:,:,1].T,c='k',alpha=0.1)
plt.plot(train_data[:,:,0].T,train_data[:,:,2].T,c='k',alpha=0.1)
# plt.show()

X_train = train_data.reshape(np.shape(train_data)[0]*np.shape(train_data)[1],np.shape(train_data)[2])
random_state = check_random_state(0)
n_components = 5
initial_means = kmeansplusplus_initialization(X_train,n_components,random_state)
initial_covs = covariance_initialization(X_train,n_components)

bgmm = BayesianGaussianMixture(n_components=n_components,max_iter=200).fit(X_train)
gmm = GMM(n_components=n_components,
          priors=bgmm.weights_,
          means=bgmm.means_,
          covariances=bgmm.covariances_,
          random_state=random_state)

test_data = train_data[10,:,:]
max_fz_0 = np.max(test_data[0:50,1])
phase_max_fz_0 = np.argmax(test_data[0:50,1])
max_fz_1 = np.max(test_data[50:, 1])
phase_max_fz_1 = np.argmax(test_data[50:,1])+50

via_fz = [0,max_fz_0, max_fz_1,0]
via_phase = [0, phase_max_fz_0, phase_max_fz_1, 0]

for fz, phase in zip(via_fz,via_phase):
    condition_gmm = gmm.condition