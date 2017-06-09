import numpy as np
import sys

# Change path as necessary
tr = np.loadtxt("../Data/satimages/sat.trn")
ts = np.loadtxt("../Data/satimages/sat.tst")

#   Define positive class, negative class
posclass = 3
negclass = 7

X = tr[:,0:36]
Y = tr[:,36]

pmask = Y == posclass
nmask = Y == negclass
mask = np.logical_or(pmask, nmask)
Xtr = X[mask,:]
Y[pmask] = 1
Y[nmask] = 0
Ytr = Y[mask]

X = ts[:,0:36]
Y = ts[:,36]

pmask = Y == posclass
nmask = Y == negclass
mask = np.logical_or(pmask, nmask)
Xts = X[mask,:]
Y[pmask] = 1
Y[nmask] = 0
Yts = Y[mask]

np.save("../Data/satimages/Xtrain.npy", Xtr)
np.save("../Data/satimages/Ytrain.npy", Ytr)
np.save("../Data/satimages/Xtest.npy", Xts)
np.save("../Data/satimages/Ytest.npy", Yts)
