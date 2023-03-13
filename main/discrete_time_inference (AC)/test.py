import numpy as np
import scipy.io

data = scipy.io.loadmat('../Data/AC.mat')
Exact = np.real(data['uu']).T
print(data['uu'])