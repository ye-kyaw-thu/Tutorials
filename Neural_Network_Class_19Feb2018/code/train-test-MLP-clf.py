from random import random
from sklearn import metrics
from matplotlib import pyplot as plt
import os
import sys
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import pickle

# Testing  MLP image classification
# Last updated: 8 Nov 2017
# Written by Ye, OPU, Japan 
# How to run: 
# python ./train-test-MLP-clf.py ./data/data.feature 

#load the csv file as a numpy matrix
dataset = np.loadtxt(sys.argv[1], delimiter=',')
#dataset = np.loadtxt('/home/lar/experiment/obj-recog2/10obj/data1/train/totoro/totoro.feature', delimiter=',')
print(dataset.shape)

# separate the data
X = dataset[:,0:4096]
y = dataset[:,4096]

#print (y)

#np.set_printoptions(threshold=np.nan)
print('Training features, X:', X)
print('===============')
print('Training labels, y:', y)
print('===============')

# splitting training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=30)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)

print('Test labels, y_test:', y_test)
#exit()
y_train = y_train.astype('int')
y_test = y_test.astype('int')
#print("X.describe: ", X.describe())
#print("y.describe: ", y.describe())

from sklearn.neural_network import MLPClassifier

#ref
#mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)

#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(20,20,20), random_state=1, max_iter=300, verbose=300)

print ('parameter:\n', clf.get_params, '\n')
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
#print ('Predit result:\n', predictions, '\n')
print (clf.predict(X_test))
#exit()

print("Training set score: %f" % clf.score(X_train, y_train))
print("Test set score: %f" % clf.score(X_test, y_test))

fig, axes = plt.subplots(4, 4)
# use global min / max to ensure all weights are shown on the same scale
vmin, vmax = clf.coefs_[0].min(), clf.coefs_[0].max()
for coef, ax in zip(clf.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(1, 4096), cmap=plt.cm.gray, vmin=.5 * vmin,
               vmax=.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

#plt.show()

#for printing all value of theta_ and sigma_
np.set_printoptions(threshold=np.inf)

print('dir(clf):\n', dir(clf), '\n')
print('clf.score: ', clf.score)
print('clf.predict_proba', clf.predict_proba)

print(' standard deviation : ', X_train.std()) 

from sklearn.metrics import confusion_matrix

y_pred_gnb = clf.fit(X_train, y_train).predict(X_test)
cnf_matrix_gnb = confusion_matrix(y_test, y_pred_gnb)
 
print("Confusion Matrix of Multilayer Perception: \n", cnf_matrix_gnb)
#exit()

#Join a sequence of arrays along a new axis.
#print(np.stack((gtheta, gsigma), axis=-1))
#exit()
print ('Predit result:\n', predictions, '\n')
print("MLP clf.score: ", clf.score(X_test, y_test))
print("===========")

from sklearn.metrics import accuracy_score

preds=clf.predict(X_test)

# Evaluate accuracy
print(accuracy_score(y_test, preds))

MLP_cv_scores = cross_val_score(clf, X, y.astype('int'), cv=10)
print("MLP Cross Validation Score: ", MLP_cv_scores)


########

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,preds))

#Saving a classifier model into a file

filename = 'ucsy-fs-MLP.4096.model'
pickle.dump(clf, open(filename, 'wb'))

