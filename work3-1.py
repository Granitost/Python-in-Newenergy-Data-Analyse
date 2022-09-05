# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:52:52 2022

@author: zxdft
"""

def isPrimeNumber(num):
    if num==1:
        return (1)
    for j in range(2,num):
        if num%j==0:
            return(0)
        while j>num/2:
            return(1)
print(isPrimeNumber(23))