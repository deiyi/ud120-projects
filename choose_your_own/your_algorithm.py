#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from time import time

def showResults(clf , name, fittingTime , predTime):
    print "\n" , name
    print "Accuracy: " , clf.score(features_test, labels_test)
    print "Fitting time: " , fittingTime
    print "Prediction time: " , predTime
    
    try:
        prettyPicture(clf, features_test, labels_test).show()
    except NameError:
        pass

def algorithmFitPredAndShow(clf , name):
    t0 = time()
    clf.fit(features_train, labels_train)
    t1 = time()
    pred = clf.predict(features_test)
    t2 = time()
    showResults(clf , name , t1 - t0 , t2 - t1)

def kNeighborsClassifierAlgorithm():
    from sklearn import neighbors   
    algorithmFitPredAndShow(neighbors.KNeighborsClassifier() , "KNeighborsClassifier") 
 
def adaBoostClassifierAlgorithm():
    from sklearn import ensemble 
    algorithmFitPredAndShow(ensemble.AdaBoostClassifier() , "AdaBoostClassifier")

def randomForestClassifierAlgorithm():
    from sklearn import ensemble 
    algorithmFitPredAndShow(ensemble.RandomForestClassifier() , "RandomForestClassifier")

kNeighborsClassifierAlgorithm()
adaBoostClassifierAlgorithm()
randomForestClassifierAlgorithm()