'''
This file converts the MNIST data into a binary classification 
dataset suitable for our library.
'''
#   This is necessary to import our modules

import numpy as np
import mnist_input as test

#   Set positive and negative class labels here
posclass = 4
negclass = 7

train_data, train_labels, test_data, test_labels, validation_data, validation_labels = test.get_data()

shape = train_data.shape
train_data = np.reshape(train_data, (shape[0], shape[1]*shape[2]))
shape = test_data.shape
test_data = np.reshape(test_data, (shape[0], shape[1]*shape[2]))
Xtr = []
Ytr = []
Xte = []
Yte = []
for i, data in enumerate(train_data):
    if train_labels[i][posclass] == 1:
        Xtr.append(data)
        Ytr.append(0)
    elif train_labels[i][negclass] == 1:
        Xtr.append(data)
        Ytr.append(1)

for i, data in enumerate(test_data):
    if test_labels[i][posclass] == 1:
        Xte.append(data)
        Yte.append(0)
    elif test_labels[i][negclass] == 1:
        Xte.append(data)
        Yte.append(1)

Xtr = np.array(Xtr)
Ytr = np.array(Ytr)
Xte = np.array(Xte)
Yte = np.array(Yte)

print Xtr.shape, Ytr.shape, Xte.shape, Yte.shape

np.save("../Data/mnist/Xtrain.npy", Xtr)
np.save("../Data/mnist/Xtest.npy", Xte)
np.save("../Data/mnist/Ytrain.npy", Ytr)
np.save("../Data/mnist/Ytest.npy", Yte)
