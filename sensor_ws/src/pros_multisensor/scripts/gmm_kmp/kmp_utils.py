import numpy as np
from numba import njit

def insert_via_point(phase, data, sigma,
                     via_phase, via_point, via_sigma,
                     via_flag):
    """
    :param phase:
    :param data:
    :param sigma:
    :param via_phase:
    :param via_point:
    :param via_sigma:
    :param via_flag:
    :return:
    """
    newData = np.copy(data)
    newSigma = np.copy(sigma)
    newPhase = np.copy(phase)
    for i in range(len(via_flag)):
        if via_flag[i] == 1:
            # replace this via point
            phase_need_to_replace = via_phase[i]
            can_replace_in = False
            replace_num = 0
            for j in range(len(phase)):
                if np.abs(phase[j] - phase_need_to_replace) < 0.0005:
                    can_replace_in = True
                    replace_num = j
                    break
            if can_replace_in:
                newPhase[replace_num] = via_phase[i]
                newData[replace_num, :] = via_point[i, :]
                newSigma[replace_num, :] = via_sigma
            else:
                # interp to the end
                newPhase = np.hstack((newPhase, via_phase[i]))
                newData = np.vstack((newData, via_point[i, :]))
                newSigma = np.vstack((newSigma, np.shape(via_sigma)))
    return newPhase, newData, newSigma


def fast_insert_via_point(phase, data, sigma, 
                          via_phase, via_point, via_sigma,
                          via_idx,via_flag):
    newData = np.copy(data)
    newSigma = np.copy(sigma)
    newPhase = np.copy(phase)
    for i in range(len(via_idx)):
        if via_flag[i]==1:
            replace_num = via_idx[i]
            newPhase[replace_num] = via_phase[i]
            newData[replace_num, :] = via_point[i, :]
            newSigma[replace_num, :] = via_sigma
    return newData, newSigma, newPhase





@njit
def kernel_extend(ta=None, tb=None, h=None, dim=None):
    # this file is used to generate a kernel value
    # this kernel considers the 'dim-' pos and 'dim-' vel

    ## callculate different kinds of kernel
    dt = 0.001
    tadt = ta + dt
    tbdt = tb + dt
    kt_t = np.exp(- h * (ta - tb) * (ta - tb))

    kt_dt_temp = np.exp(- h * (ta - tbdt) * (ta - tbdt))

    kt_dt = (kt_dt_temp - kt_t) / dt

    kdt_t_temp = np.exp(- h * (tadt - tb) * (tadt - tb))

    kdt_t = (kdt_t_temp - kt_t) / dt

    kdt_dt_temp = np.exp(- h * (tadt - tbdt) * (tadt - tbdt))

    kdt_dt = (kdt_dt_temp - kt_dt_temp - kdt_t_temp + kt_t) / dt / dt

    kernelMatrix = np.zeros((2 * dim, 2 * dim))

    for i in range(dim):
        kernelMatrix[i, i] = kt_t
        kernelMatrix[i, i + dim] = kt_dt
        kernelMatrix[i + dim, i] = kdt_t
        kernelMatrix[i + dim, i + dim] = kdt_dt

    return kernelMatrix

@njit
def kmp_estimateMatrix_mean(phase, data, sigma, kh, lamda):
    D = np.shape(data)[1]
    n_dim = int(D / 2)
    n_sample = np.shape(data)[0]
    kc = np.zeros((D * n_sample, D * n_sample))
    for i in range(n_sample):
        for j in range(n_sample):
            
            dim = n_dim
            ta = phase[i]
            tb = phase[j]
            h = kh
            dt = 0.001
            tadt = ta + dt
            tbdt = tb + dt
            kt_t = np.exp(- h * (ta - tb) * (ta - tb))

            kt_dt_temp = np.exp(- h * (ta - tbdt) * (ta - tbdt))

            kt_dt = (kt_dt_temp - kt_t) / dt

            kdt_t_temp = np.exp(- h * (tadt - tb) * (tadt - tb))

            kdt_t = (kdt_t_temp - kt_t) / dt

            kdt_dt_temp = np.exp(- h * (tadt - tbdt) * (tadt - tbdt))

            kdt_dt = (kdt_dt_temp - kt_dt_temp - kdt_t_temp + kt_t) / dt / dt

            kernelMatrix = np.zeros((2 * dim, 2 * dim))

            for k in range(dim):
                kernelMatrix[k, k] = kt_t
                kernelMatrix[k, k + dim] = kt_dt
                kernelMatrix[k + dim, k] = kdt_t
                kernelMatrix[k + dim, k+ dim] = kdt_dt

            # kc[i * D:(i + 1) * D, j * D:(j + 1) * D] = kernel_extend(phase[i], phase[j], kh, n_dim)
            kc[i * D:(i + 1) * D, j * D:(j + 1) * D] = kernelMatrix
            if i == j:
                C_temp = sigma[i, :].reshape((D, D))
                kc[i * D:(i + 1) * D, j * D:(j + 1) * D] += lamda * C_temp
    return np.linalg.inv(kc)

@njit
def kmp_pred_mean(phase_current, phase_ref, data, kh, Kinv):
    D = np.shape(data)[1]
    n_dim = int(D / 2)
    n_sample = np.shape(data)[0]
    k = np.zeros((D, D * n_sample))
    Y = np.zeros((D * n_sample, 1))
    for i in range(n_sample):
        k[0:D, i * D:(i + 1) * D] = kernel_extend(phase_current, phase_ref[i], kh, n_dim)
        for h in range(D):
            Y[i * D + h] = data[i, h]
    Mu = k @ Kinv @ Y
    return Mu.reshape((-1,))

def kmp_interp_with_phase(phase_new, phase_ref, data_ref, kh, Kinv):
    mu_list = []
    for i in range(np.shape(phase_new)[0]):
        mu = kmp_pred_mean(phase_current=phase_new[i],
                           phase_ref=phase_ref,
                           data=data_ref,
                           kh=kh,
                           Kinv=Kinv)
        mu_list.append(mu)
    return np.array(mu_list)
