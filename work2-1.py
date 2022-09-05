# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:46:53 2022

@author: zxdft
"""
def func1():
    num=int(input("请输入3位正整数"))
    position3=num%10
    position2=(num%100)/10
    position1=int(num/100)
    print("个位：",position3)
    print("十位：",int(position2))
    print("百位：",position1)
#func1()



def func2():
    num=int(input("请输入一个整数"))
    square=num**2
    squareRoot=num**0.5
    cube=num**3
    cubeRoot=num**(1/3)
    print("square:",square)
    print("squareRoot:",squareRoot)
    print("cube:",cube)
    print("cubeRoot:",cubeRoot)
#func2()
    
    
    
import math
def func3():
    angle=30
    radian=(angle/180)*3.14
    sin=math.sin(radian)
    cos=math.cos(radian)
    print("sin",angle,"=",sin)
    print("cos",angle,"=",cos)
#func3()
    
    
    
def func4():
    def total(a,b,c):
        total=a+b+c
        return(total)
    def average(a,b,c):
        average=(a+b+c)/3
        return(average)
    def markAnalization(a,b,c):
        print(total(a,b,c))
        print(average(a,b,c))
    markAnalization(98,100,99)
#func4()
        


def func5():
    radiu=float(input("输入球的半径"))
    volume=(4/3)*3.14*radiu**3
    print("体积：%.1f"%volume)
#func5()
    
    
    
def func6():
    letter=input("输入大写字母")
    lowerLetter=letter.lower()
    print(lowerLetter)
#func6()