# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:40:40 2018

@author: Zhong-Ying Wang
"""

import numpy as np
import math
from sklearn import svm
import csv
from sklearn.model_selection import train_test_split  #from sklearn.cross_validation import train_test_split 更新sklearn前的
import re
from sklearn.preprocessing import StandardScaler
import copy

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
array_temp3 = []

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
        #print(temp)
              
    #print(array_temp)
    

#print(array_temp)
#print(len(array_temp))

    
# print(array)
#print(array_temp[2][0])


#type(array_temp[2][0])


train, train_target= turn_to_train(array_temp)
test, test_target= turn_to_test(array_temp)

clf = svm.SVC()
clf.fit(train,train_target)

result = clf.predict(test)


print(result)
print(len(result))

print(clf.score(test, test_target))
#print (clf.support_)

#-------------------------購過 PCA -------------------------------------#
array_temp2 = copy.deepcopy(array_temp)

array_temp2 = del_array(array_temp2)

from sklearn.decomposition import PCA
pca = PCA(n_components = 8)
#pca.fit(array_temp)

array = pca.fit_transform(array_temp2)
print(len(array))
train2, train_target2 = turn_to_train(array)
test2, test_target2 = turn_to_test(array)

clf = svm.SVC()
clf.fit(train2,train_target)

result2 = clf.predict(test2)

print(result2)
print(len(train2),"  ",len(train_target2),"  ",len(test2),"  ",len(test_target2))
print(len(result2))

print(clf.score(test2, test_target))

#------------------------手動拔掉不需要的維度-----------------------------#
#----------------21(電話) 10(個人身分+性別) 23(外國工人) 9(年齡) 1(月份持續時間) 3(貸款目的)

array_temp3 = copy.deepcopy(array_temp)

for i in range(0,len(array_temp)):
    del array_temp3[i][23]
    del array_temp3[i][21]
    del array_temp3[i][10]
    del array_temp3[i][9]
    del array_temp3[i][3]
    del array_temp3[i][1]

    

train, train_target= turn_to_train(array_temp3)
test, test_target= turn_to_test(array_temp3)

clf = svm.SVC()
clf.fit(train,train_target)

result = clf.predict(test)


print(result)
print(len(result))

print(clf.score(test, test_target))



