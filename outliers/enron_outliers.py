#!/usr/bin/python

import pickle
import sys
import numpy as np
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)
array=np.array([["salary"],["bonus"]])
### your code below
salary=[]
for i in data_dict.keys():
    if data_dict[i]['salary']=='NaN':
    	salary.append(0)
    else:
    	salary.append(int(data_dict[i]['salary']))
bonus=[]
for i in data_dict.keys():
    if data_dict[i]['bonus']=='NaN':
    	bonus.append(0)
    else:
    	bonus.append(int(data_dict[i]['bonus']))

max_salary=max(salary)
max_bonus=max(bonus)

for i in data_dict.keys():
	if data_dict[i]['salary']==max_salary and data_dict[i]['bonus']==max_bonus:
		print(i)
for i in range(len(salary)):
	if salary[i]>1000000 and bonus[i]>5000000:
		print(salary[i],bonus[i])
for i in data_dict.keys():
	if data_dict[i]['salary']==1072321 and data_dict[i]['bonus']==7000000:
		print(i)
	if data_dict[i]['salary']==1111258 and data_dict[i]['bonus']==5600000:
		print(i)
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

