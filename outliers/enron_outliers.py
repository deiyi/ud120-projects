#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit



### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]


### your code below
def findMaxSalaryName(data_dict):
    maxSalary = 0
    maxBonus = 0
    maxName = ""
    for name in data_dict.keys():
        if data_dict[name]["salary"] != "NaN":
            if data_dict[name]["salary"] > maxSalary:
                maxName = name
                maxSalary = data_dict[name]["salary"]
                maxBonus = data_dict[name]["bonus"]
    print maxName, data_dict[maxName]["salary"], data_dict[maxName]["bonus"], " is a typo."
    
    return maxName  

data_dict.pop(findMaxSalaryName(data_dict) , 0)
data = featureFormat(data_dict, features)

for name in data_dict.keys():
    if data_dict[name]["bonus"] != "NaN" and data_dict[name]["salary"] != "NaN":
        if data_dict[name]["bonus"] > 5e6 and data_dict[name]["salary"] > 1e6:
            print name, data_dict[name]["salary"], data_dict[name]["bonus"]  

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()