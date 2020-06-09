#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score
from time import time
import matplotlib.pyplot as plt

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train=features_train[:(len(features_train)//100)]
# labels_train=labels_train[:len(labels_train)//100]
clf=svm.SVC(C=10000.0,gamma='auto',kernel='rbf')
t0=time()
clf.fit(features_train,labels_train)
plt=clf.fit(features_train,labels_train)
print("train",round(time()-t0,3))
t1=time()
pred=clf.predict(features_test)
print("pred",round(time()-t1,3))
print(accuracy_score(pred,labels_test))
# print(pred[10])
# print(pred[26])
# print(pred[50])
# plt.show()
count = 0
for i in range(len(pred)):
	if(pred[i]==1):
		count=count+1
print(count)




#########################################################
### your code goes here ###

#########################################################


