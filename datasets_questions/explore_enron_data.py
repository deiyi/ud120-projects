#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Total length: " , len(enron_data)
print "Total characteristics: " , len(enron_data[enron_data.keys()[1]])

poi = 0
for name in enron_data.keys():
    poi += enron_data[name]["poi"]
print "POI: " , poi

# print enron_data.keys()
for name in enron_data.keys():
    if name.find("PRENTICE") != -1:
        print "total_stock_value for PRENTICE: " , enron_data[name]["total_stock_value"]

for name in enron_data.keys():
    if name.find("COLWELL") != -1:
        print "from_this_person_to_poi for COLWELL: " , enron_data[name]["from_this_person_to_poi"]
        
for name in enron_data.keys():
    if name.find("SKILLING") != -1:
        print "exercised_stock_options for SKILLING: " , enron_data[name]["exercised_stock_options"]
        
for person in ["LAY" , "SKILLING" , "FASTOW"]:
    for name in enron_data.keys():
        if name.find(person) != -1:
            print "total_payments for " , person , ": " , enron_data[name]["total_payments"]        
        
amountSalary = 0
amountEmail = 0
amountTotalPay = 0
poiAmount = 0
poiAndNaNAmount = 0
for name in enron_data.keys():
    if enron_data[name]["salary"] != "NaN":
        amountSalary += 1
    if enron_data[name]["email_address"] != "NaN":
        amountEmail += 1
    if enron_data[name]["total_payments"] == "NaN":
        amountTotalPay += 1
    if enron_data[name]["poi"] == True:
        poiAmount += 1
    if (enron_data[name]["poi"] == True) and (enron_data[name]["total_payments"] == "NaN"):
        poiAndNaNAmount += 1
print "amount of people with salary NaN: " , amountSalary
print "amount of people with e-mail NaN: " , amountEmail      
print "amount of people with total payment NaN: " , amountTotalPay 
print "% Total payment NaN:" ,  float(amountTotalPay) / float(len(enron_data)) * 100
print "Total length: " , len(enron_data)     
print "POI amount: " , poiAmount     
print "poiAndNaNAmount amount: " , poiAndNaNAmount  

# C:\ProgramData\Anaconda27\python.exe explore_enron_data.py
        