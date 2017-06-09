import numpy as np

conv = {0: lambda s: ord(s.strip()) - 65}
# Change path as per need
tr = np.loadtxt("../Data/letter/letter-recognition.data", converters=conv, delimiter=",")

#   Define positive class, negative class
posclass = 0
negclass = 10

X = tr[0:16000:,1:17]
Y = tr[0:16000:,0]

pmask = Y == posclass
nmask = Y == negclass
mask = np.logical_or(pmask, nmask)
Xtr = X[mask,:]
Y[pmask] = 1
Y[nmask] = 0
Ytr = Y[mask]


X = tr[16000:20000,1:17]
Y = tr[16000:20000,0]

pmask = Y == posclass
nmask = Y == negclass
mask = np.logical_or(pmask, nmask)
Xts = X[mask,:]
Y[pmask] = 1
Y[nmask] = 0
Yts = Y[mask]

np.save("../Data/letter/Xtrain.npy", Xtr)
np.save("../Data/letter/Ytrain.npy", Ytr)
np.save("../Data/letter/Xtest.npy", Xts)
np.save("../Data/letter/Ytest.npy", Yts)
