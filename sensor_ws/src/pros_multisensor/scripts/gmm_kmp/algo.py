from gmm_kmp.gmm_utils import *
from gmm_kmp.kmp_utils import *
import pickle
from scipy.ndimage import gaussian_filter1d
import scipy.interpolate as scip
from numba import njit

@njit
def other_func():
    return 1
class gmm_kmp_fp_pipeline:
    def __init__(self):
        self.idx_fz_max_0_default = 25
        self.idx_fz_max_1_default = 75 
        self.idx_fz_mid_st_default = 50
        self.via_idx = []
        self.via_point = []
        self.via_sigma = np.eye(4)*1e-6
        self.DataRef = []
        self.SigmaRef = []
        self.Phase = []
        self.stance_cubic = []
        self.init_gmm_ref()
        self.fz_rebuild = []
        self.fx_rebuild = []


    def init_gmm_ref(self):
        model = "/home/yuxuan/Project/Pros_Ctrl/sensor_ws/src/pros_multisensor/scripts/gmm_kmp/fp_gmm"
        gmm = pickle.load(open(model,"rb"))
        self.Phase = np.linspace(0,1,100)
        self.DataRef, self.SigmaRef = gmm_Interp_with_phase(gmm, self.Phase)
        other_func()
        
    def find_peak_and_valley(self):
        idx_fea = [0,0,0]
        is_fea_find = [False, False, False]
        idx_all = np.arange(0,100).astype('uint8')
        idx_fz_max = np.argmax(self.stance_cubic)
        fz_max = self.stance_cubic[idx_fz_max]
        if idx_fz_max >= 60 and idx_fz_max <=90:
            idx_fea[2] = idx_fz_max
            is_fea_find[2] = True
            idx_fz_sub_max = np.argmax(self.stance_cubic[0:45])
            fz_sub_max = self.stance_cubic[idx_fz_sub_max]
            if idx_fz_sub_max<=45 and idx_fz_sub_max >=10:
                mid_stance = self.stance_cubic[idx_fz_sub_max:idx_fz_max]
                idx_fz_mid_min = np.argmin(mid_stance)# attention: idx_fz_mid_min is relative to the mid stance interval not stance_cubic
                fz_mid_min = mid_stance[idx_fz_mid_min]
                if idx_fz_mid_min > (idx_fz_max-idx_fz_sub_max)*0.2 and idx_fz_mid_min < (idx_fz_max-idx_fz_sub_max)*0.9:
                    if fz_mid_min < fz_max*0.6:
                        idx_fea[0] = idx_fz_sub_max
                        is_fea_find[0] = True
                        idx_fea[1] = idx_fz_sub_max+idx_fz_mid_min
                        is_fea_find[1] = True
                else:
                    if fz_mid_min < fz_max*0.6: 
                        if fz_sub_max - fz_mid_min > 0.05:
                            idx_fea[0] = idx_fz_sub_max
                            is_fea_find[0] = True
                            idx_fea[1] = 0
                            is_fea_find[1] = False

        elif idx_fz_max <=45 and idx_fz_max >=10:
            idx_fea[0] = idx_fz_max
            is_fea_find[0] = True
            idx_fz_sub_max = np.argmax(self.stance_cubic[60:])
            idx_fz_sub_max = idx_fz_max+60
            fz_sub_max = self.stance_cubic[idx_fz_sub_max]
            if idx_fz_sub_max>=60 and idx_fz_sub_max<=90:
                mid_stance = self.stance_cubic[idx_fz_max:idx_fz_sub_max]
                idx_fz_mid_min = np.argmin(mid_stance)# attention: idx_fz_mid_min is relative to the mid stance interval not stance_cubic
                fz_mid_min = mid_stance[idx_fz_mid_min]
                if idx_fz_mid_min > (idx_fz_sub_max-idx_fz_max)*0.2 and idx_fz_mid_min < (idx_fz_sub_max-idx_fz_max)*0.9:
                    if fz_mid_min < fz_max*0.8:
                        idx_fea[2] = idx_fz_sub_max
                        is_fea_find[2] = True
                        idx_fea[1] = idx_fz_max+idx_fz_mid_min
                        is_fea_find[1] = True
                        return idx_fea, is_fea_find
                else:
                    if fz_mid_min < fz_max*0.6: 
                        if fz_sub_max - fz_mid_min > 0.05:
                            idx_fea[2] = idx_fz_sub_max
                            is_fea_find[2] = True
                            idx_fea[1] = 0
                            is_fea_find[1] = False
        return idx_fea, is_fea_find
    
    def generate_via_points_from_feature(self,idx_fea, is_fea_find):
        self.via_point = np.zeros((5,4))
        if not is_fea_find[0] and not is_fea_find[2]:
            max_fz = np.max(self.stance_cubic)
            self.via_idx = [0,self.idx_fz_max_0_default,
                                self.idx_fz_mid_st_default,
                                self.idx_fz_max_1_default,99]
            self.via_point[:,0] = np.array([0,max_fz*0.9,max_fz*0.6,max_fz,0])
            self.via_point[:,1] = self.DataRef[self.via_idx,1]
            self.via_point[:,3] = self.DataRef[self.via_idx,3]
        elif not is_fea_find[0] and is_fea_find[2]:
            max_fz = self.stance_cubic[idx_fea[2]]
            self.via_idx = [0,
                                self.idx_fz_max_0_default,
                                int((idx_fea[2]+self.idx_fz_max_0_default)/2),
                                idx_fea[2],
                                99]
            self.via_point[:,0] = np.array([0,max_fz*0.9,max_fz*0.8,max_fz,0])
            self.via_point[:,1] = self.DataRef[self.via_idx,1]
            self.via_point[:,3] = self.DataRef[self.via_idx,3]
        elif is_fea_find[0] and not is_fea_find[2]:
            max_fz = self.stance_cubic[idx_fea[0]]
            self.via_idx = [0,
                                idx_fea[0],
                                int((idx_fea[0]+self.idx_fz_max_1_default)/2),
                                self.idx_fz_max_1_default,
                                99]
            self.via_point[:,0] = np.array([0,max_fz,max_fz*0.8,max_fz,0])
            self.via_point[:,1] = self.DataRef[self.via_idx,1]
            self.via_point[:,3] = self.DataRef[self.via_idx,3]
        elif is_fea_find[0] and not is_fea_find[1] and is_fea_find[2]:
            max_fz0 = self.stance_cubic[idx_fea[0]]
            max_fz1 = self.stance_cubic[idx_fea[2]]
            self.via_idx = [0,
                                idx_fea[0],
                                int((idx_fea[0]+idx_fea[2])/2),
                                idx_fea[2],
                                99]
            self.via_point[:,0] = np.array([0,max_fz0,
                                            max(max_fz0,max_fz1)*2-min(max_fz0,max_fz1)
                                            ,max_fz1,0])
            self.via_point[:,1] = self.DataRef[self.via_idx,1]
            self.via_point[:,3] = self.DataRef[self.via_idx,3]
        elif is_fea_find[0] and is_fea_find[1] and is_fea_find[2]:
            max_fz0 = self.stance_cubic[idx_fea[0]]
            mid_fz = self.stance_cubic[idx_fea[1]]
            max_fz1 = self.stance_cubic[idx_fea[2]]
            self.via_idx = [0,
                                idx_fea[0],
                                idx_fea[1],
                                idx_fea[2],
                                99]
            self.via_point[:,0] = np.array([0,max_fz0,mid_fz,max_fz1,0])
            self.via_point[:,1] = self.DataRef[self.via_idx,1]
            self.via_point[:,3] = self.DataRef[self.via_idx,3]
        

    def extract_fea(self, stance_vec):
        stance_filter = gaussian_filter1d(stance_vec,2)
        n_sample = np.shape(stance_filter)[0]
        x = np.linspace(0,1,n_sample)
        xx = self.Phase
        interp_fun =  scip.interp1d(x,stance_filter,kind='cubic')
        self.stance_cubic = interp_fun(xx)
        self.stance_cubic[0] = 0
        self.stance_cubic[-1] = 0
        idx_fea, is_fea_find = self.find_peak_and_valley()
        self.generate_via_points_from_feature(idx_fea, is_fea_find)

    def fast_fea(self, stance_vec):
        stance_filter = gaussian_filter1d(stance_vec,2)
        n_sample = np.shape(stance_filter)[0]
        x = np.linspace(0,1,n_sample)
        xx = self.Phase
        interp_fun =  scip.interp1d(x,stance_filter,kind='cubic')
        self.stance_cubic = interp_fun(xx)
        self.stance_cubic[0] = 0
        self.stance_cubic[-1] = 0
        self.via_point = np.zeros((10,4))
        idx_fea = np.arange(0,99,10).astype('int')
        idx_fea[-1] = 99
        dx = x[1]-x[0]
        stance_cubic_d = np.gradient(self.stance_cubic)/dx
        self.via_point[:,0] = self.stance_cubic[idx_fea]
        self.via_point[:,1] = self.DataRef[idx_fea,1]
        self.via_point[:,2] = stance_cubic_d[idx_fea]
        self.via_point[:,3] = self.DataRef[idx_fea,3]
        self.via_idx = idx_fea


    def kmp_rebuild(self):
        via_phase = self.Phase[self.via_idx]
        newData, newSigma, newPhase = fast_insert_via_point(phase=self.Phase,
                                                          data=self.DataRef,
                                                          sigma=self.SigmaRef,
                                                          via_phase = via_phase,
                                                          via_point=self.via_point,
                                                          via_sigma=self.via_sigma,
                                                          via_idx=self.via_idx,
                                                          via_flag=[1,1,1,1,1]
                                                          )
        kh = 10
        print("KMP_Start")
        Kinv = kmp_estimateMatrix_mean(phase=newPhase,
                                       data=newData,
                                       sigma=newSigma,
                                       kh = kh,
                                       lamda=1)
        print("KMP1 Finish")
        fianlTraj = kmp_interp_with_phase(phase_new=self.Phase,
                                          phase_ref=self.Phase,
                                          data_ref=newData,
                                          kh = kh,
                                          Kinv = Kinv)
        print("KMP2 Finish")
        self.fz_rebuild = fianlTraj[:,0]
        self.fz_rebuild[0] = 0
        self.fz_rebuild[-1] = 0
        self.fx_rebuild = fianlTraj[:,1]
        self.fx_rebuild[0] = 0
        self.fx_rebuild[-1] = 0