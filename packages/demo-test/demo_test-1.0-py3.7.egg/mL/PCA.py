# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:10:21 2018

@author: Zhong-Ying Wang
"""

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
        
array_temp2 = array_temp

print(len(array_temp2))

array_temp2 = del_array(array_temp2)

print(len(array_temp2[0]))

from sklearn.decomposition import PCA
pca = PCA(n_components = 10, copy=True, whiten=False)
#pca.fit(array_temp)

array = pca.fit_transform(array_temp)

print(len(array))

print(len(array_temp[::][:24]))

train, train_target= turn_to_train(array_temp)
test, test_target= turn_to_test(array_temp)
