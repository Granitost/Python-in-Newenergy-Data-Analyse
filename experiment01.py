# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 17:24:42 2022

@author: zxdft
"""

def func1():
    inputNumbers=list([0,0,0])
    for i in range(0,3):
        inputNumbers[i]=int(input('请输入参与比较的整数'))
    inputNumbers.sort(reverse=True)
    print('\n最大数为：',inputNumbers[0])
#func1()
    
    
    
def func2():
    age=int(input('请输入年龄'))
    if(age<0):
        print('请输入有效年龄')
    elif 0<=age<=17:
        print('未成年人')
    elif 18<=age<=65:
        print('青年人')
    elif 66<=age<=79:
        print('中年人')
    elif 80<=age<=99:
        print('老年人')
    else:
        print('长寿老人')
#func2()



def func3():
    triangle=[0,0,0]
    triEqual=0
    equal=0
    for i in range(0,3):
        triangle[i]=int(input('请输入边'))
    for j in range(0,3):
        test=(triangle[j]+triangle[j-1])>triangle[j-2]
        if test==False:
            break
    if test!=False:
        triangle.sort()
        if triangle[0]==triangle[1]==triangle[2]:
            print('\n等边三角形')
            triEqual=True
        else:
            for i in range (0,3):
                if triangle[i]==triangle[i-1]:
                    print('\n等腰三角形')
                    equal=True
        if triangle[0]**2+triangle[1]**2==triangle[2]**2:
            print('\n直角三角形')
        else:
            if(triEqual!=True|equal!=True):
                print('\n一般三角形')
    else:
        print('\n无法构成三角形')
#func3()
        
        
        
def func4(distance):
    fee=99999999
    if 0<distance<100:
        fee=1000
    elif 100<=distance<=500:
        fee=1000+(distance-100)*3.5
    elif distance>500:
        fee=1000+(distance-100)*5
    else:
        fee='error'
    print('运费为：',fee)
#func4(float(input('请输入公里数')))
    
    
    
def func5():
    for i in range(100,1000):
        if (i//100)**3+((i%100)//10)**3+(i%10)**3==i:
            print(i)
#func5()
            
            
            
def func6():
    c="Python is a programming langange."
    newC=c.replace(" ","\\")
    print('\n',newC)
#func6()
    
    
    
def func7():
    import random
    marks=[]
    for i in range(0,10):
        marks.append(random.randint(0,100))
    print('前',marks)
    marks.sort(reverse=True)
    print('后',marks)
#func7()
    
    
    
def func8():
    for i in range(0,4):
        print(' '*(3-i),end='')
        for j in range(1,i+2):
            print(j,end='')
        for k in range(0,i):
            print(3-k,end='')
        print('\r')
    print('\n')
    num=65
    for i in range(0,4):
        for j in range(0,7-2*i,1):
            if j==6:
                continue
            alpha=chr(num)
            print(alpha,end='')
        num+=1
        print('\r')
func8()