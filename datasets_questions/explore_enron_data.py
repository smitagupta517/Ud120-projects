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
import pandas as pd

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print(len(enron_data))
feat=list(enron_data.keys())
print(len(enron_data[feat[0]]))
print(enron_data[feat[0]])
count=0
for i in range(len(enron_data)):
	if enron_data[feat[i]]['poi']==1:
		count=count+1
print(count)

print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print(enron_data["LAY KENNETH L"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])
print(enron_data["SKILLING JEFFREY K"]["total_payments"])

test=0
for i in range(len(enron_data)):
	if enron_data[feat[i]]["salary"]!='NaN':
		test=test+1
print(test)

# temp=0
# for i in range(len(enron_data)):
# 	if enron_data[feat[i]]["email_address"]!='NaN':
# 		temp=temp+1
# print(temp)

# temp1=0
# for i in range(len(enron_data)):
# 	if enron_data[feat[i]]["total_payments"]=='NaN':
# 		temp1=temp1+1
# print(temp1)

temp1=0
for i in range(len(enron_data)):
	if enron_data[feat[i]]["poi"]==1 and enron_data[feat[i]]["total_payments"]=='NaN':
		temp1=temp1+1
print(temp1)