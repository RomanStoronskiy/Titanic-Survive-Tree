'''import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier

X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])
clf = DecisionTreeClassifier()
clf.fit(X, y)
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked



data = pandas.read_csv('titanic.csv')
survived = data['Survived']
signs = data.drop(data.columns[[0,1,3,6,7,8,10,11]], axis = 1)
signs = signs.replace('male', 1)
signs = signs.replace('famale', 0)

print(signs['Sex'])'''

import numpy as np

a = input()
a = a.split()
a = a[0:2]
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(a[i],a[j],a[k])