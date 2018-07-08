#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

# C:\ProgramData\Anaconda27\python.exe evaluate_poi_identifier.py

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]
sort_keys = '../tools/python2_lesson14_keys.pkl'
data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=0.3, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print "Accuracy: " , clf.score(features_test, labels_test)

pred = clf.predict(features_test)
print "Amount of predicted POIs: " , int(sum(pred))
print "Amount of people: " , len(features_test)

countTruePos = 0
for i, feature in enumerate(features_test):
    if feature == pred[i] and pred[i] == 1:
        countTruePos = countTruePos + 1
print "Count True Positive: " , countTruePos

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
print "Precission score: " , precision_score(labels_test, pred, average=None)
print "Recall score: " , recall_score(labels_test, pred, average=None)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "Precission score: " , precision_score(true_labels, predictions, average=None)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "Recall score: " , recall_score(true_labels, predictions, average=None)
