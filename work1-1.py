# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def alpha(first,last):
    sum=0
    for i in range(first,last+1):
        sum=sum+i
    return sum
result=alpha(1,100)
print("The result is:%d"%result)
