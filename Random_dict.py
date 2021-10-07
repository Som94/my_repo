# -*- coding: utf-8 -*-
"""
2) populate 10 random numbers in the range of 1 to 1000
Store it in dict , key is first random no. And the rest are values
Repeat the above 10 times, so you have 10 keys and 90 values totally.
Process the dict and display the key with  the values having max prime.
Key is not considered for prime.
"""
from random import *

ran_list=[]
ran_dict={}
for i in range(10):
    ran_num=randint(1,1000)
    ran_list.append(ran_num)
    #ran_dict[ran_num]=[randint(1,1000) for j in range(10)]
    
for j in ran_list:
    ran_dict[j]=list(filter(lambda a : a != j, ran_list ))
    
print(ran_dict)