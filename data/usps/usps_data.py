import numpy as np

# Change path as necessary
tr = np.loadtxt("../Data/usps/zip.train")
ts = np.loadtxt("../Data/usps/zip.test")

#   Define positive class, negative class
posclass = 3
negclass = 7

X = tr[:,1:257]
Y = tr[:,0]

pmask = Y == posclass
nmask = Y == negclass
mask = np.logical_or(pmask, nmask)
Xtr = X[mask,:]
Y[pmask] = 1
Y[nmask] = 0
Ytr = Y[mask]

X = ts[:,1:257]
Y = ts[:,0]

pmask = Y == posclass
nmask = Y == negclass
mask = np.logical_or(pmask, nmask)
Xts = X[mask,:]
Y[pmask] = 1
Y[nmask] = 0
Yts = Y[mask]

np.save("../Data/usps/Xtrain.npy", Xtr)
np.save("../Data/usps/Ytrain.npy", Ytr)
np.save("../Data/usps/Xtest.npy", Xts)
np.save("../Data/usps/Ytest.npy", Yts)
