#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#########################################################
### your code goes here ###
from sklearn import svm
clf = svm.SVC(kernel="rbf" , C=10000)

# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
t1 = time()
pred = clf.predict(features_test)
t2 = time()

print "Accuracy: " , clf.score(features_test, labels_test)
print "Fitting time: " , t1 - t0
print "Prediction time: " , t2 - t1
print "Prediction 10: " , pred[10]
print "Prediction 26: " , pred[26]
print "Prediction 50: " , pred[50]
print "Amount Chris: " , sum(pred)


#########################################################
# C:\ProgramData\Anaconda27\python.exe svm_author_id.py

