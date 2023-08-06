# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:40:40 2018

@author: Zhong-Ying Wang
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier  

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random

def turn_to_train(x):
    
    train = []
    target = []
    length = len(x)
    length2 = len(x[0])
    
    test_len = int(length * 8 / 10)
    
    for i in range(0,test_len):
        train.append(x[i][0:length2-1])
        target.append(x[i][length2-1])

    return train, target

def turn_to_test(x):
    
    test = []
    target = []
    length = len(x)
    length2 = len(x[0])
    
    test_len = int(length * 8 / 10)
   
    
    for i in range(test_len,length):
        test.append(x[i][0:length2-1])
        target.append(x[i][length2-1])

    return test, target

def del_array(x):
    
    length = len(x)
    length2 = len(x[0])
    
    for i in range(0,length):
        del x[i][length2-1]
        
    return x


array = []
array_temp = []
array_temp2 = []

#將list中的string轉int
#results = list(map(int, results))


with open('資料集處理過.txt','r') as f:
    
    #print(f.read())
    a = f.readlines()
    for line in a:
        
        temp = line.split()
        #temp = re.split(r'[\s]',line) 
        temp = list(map(int,temp))   
        array_temp.append(temp)


train, train_target= turn_to_train(array_temp)
test, test_target= turn_to_test(array_temp)

neigh = KNeighborsClassifier(n_neighbors=2)

neigh.fit(train,train_target) 

result = neigh.predict(test)

print(result)
print(neigh.score(test, test_target))

#-------------------------購過 PCA -------------------------------------#

array_temp2 = array_temp

array_temp2 = del_array(array_temp2)

from sklearn.decomposition import PCA
pca = PCA(n_components = 18)
#pca.fit(array_temp)

array = pca.fit_transform(array_temp2)
print(len(array))
train2, train_target2 = turn_to_train(array)
test2, test_target2 = turn_to_test(array)

neigh = KNeighborsClassifier(n_neighbors=2)

print(len(train),"  ",len(train_target),"  ",len(test),"  ",len(test_target))

neigh.fit(train2,train_target) 

result2 = neigh.predict(test2)

print(result2)
print(neigh.score(test2, test_target))
'''
cValue = ['r','y']

plt.scatter(train, train,c = cValue, cmap=plt.cm.Paired)  
plt.xlabel(u'身高')  
plt.ylabel(u'体重')  
plt.show()

'''