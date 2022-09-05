# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 17:24:42 2022

@author:Granitost
"""

def func1():
    from itertools import permutations
    alpha=[1,2,3,4]
    beta=permutations(alpha,3)
    times=0
    for i in beta:
        print(int(i[0])*100+int(i[1])*10+int(i[2]),end=' ')
        times+=1
    print('\n共有',times,'个不相同且无重复数字的三位数')
#func1()
    
    
    
def isPrimeNumber(num):
    num=int(num)
    if num==1:
        return (1)
    for j in range(2,num):
        if num%j==0:
            return(0)
        while j==num-1:
            return(1)    
    
    
def func2(start,end):
    times=0
    for i in range(start,end+1):
        if isPrimeNumber(i):
            times+=1
            print(i,end=' ')
    print('\n共有',times,'个素数')
#func2(101,200)
    
    
                
def func3(number):
    result=list([])
    def alpha(a):
        a=int(a)
        for i in range(2,a):
            if isPrimeNumber(a):
                a=int(a)
                result.append(a)
                break
            elif a%i==0:
                result.append(i)
                a=a/i
                alpha(a)
                break

    alpha(number)
    print(number,'=',end='')
    result.sort()
    for i in range(1,len(result)*2-1,2):
        result.insert(i,'*')
    for i in range(0,len(result)):
        print(result[i],end='')
#func3(int(input('请输入需要被分解的正整数')))
        
        
        
def func4(string):
    alphaCount=0
    numberCount=0
    numberSpace=0
    numberOther=0
    for i in string:
        if i.isalpha():
            alphaCount+=1
        elif i in ['1','2','3','4','5','6','7','8','9','0']:
            numberCount+=1
        elif i==' ':
            numberSpace+=1
        else:
            numberOther+=1
    print('英文字母：',alphaCount,
          '\n数字',numberCount,
          '\n空格',numberSpace,
          '\n其他字符',numberOther)
#func4(input('请输入任意字符串'))
    
    

def factorial(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    return result


def func5(start,stop):
    result=0
    for i in range(start,stop+1):
        result=result+factorial(i)
    return result
#print(func5(1,20))
    


def func6(number):
    if (int(number//10000)==number%10)&((number//1000)%10==(number%100)//10):
        print('It is.')
    else:
        print('It isn`t.')
#func6(int(input('请输入需要被判断的五位数')))
        
        
        
def func7():
    import random
    numberList=list([])
    for i in range(1,1001):
        number=random.randint(20,100)
        numberList.append(number)
    numberList.sort()
    result=dict({})
    a=0
    for i in numberList:
        if a<i:
            times=numberList.count(i)
            result[i]=times
            a=i
    print(result)
#func7()
        
    
    
def func8():
    d={"数学":105,"语文":101,"英语":98,"物理":55}
    d["化学"]=59
    d["数学"]=115
    del d["英语"]
    print(d)
func8()