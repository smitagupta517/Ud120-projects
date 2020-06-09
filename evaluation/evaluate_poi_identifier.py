#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.3,random_state=42)
count=0
for i in labels_test:
	if i==1.0:
		count+=1
print(count)
print(len(labels_test))

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
print(accuracy_score(pred,labels_test))
print(precision_score(labels_test,pred))
print(recall_score(labels_test,pred))

test=0
for i in range(len(labels_test)):
	if labels_test[i]==1.0 and pred[i]==1.0:
		test+=1
print(test)
### your code goes here 


