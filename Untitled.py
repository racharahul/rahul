#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#1. Simple calculator
a=float(input("value of a "))
b=float(input("value of b "))
print("Addition = ",a+b)
print("Substraction = ",a-b)
print("Multiplication =  ",a*b)
print("Division = ",a/b)
print("Modulus = ",a%b)
print("Exponential = ",a**b)
print("Floor Division = ",a//b)




#2. Simple Interest
P=float(input("Enter the Principle Amount"))
T=float(input("Enter the Time"))
R=float(input("Enter rate of Interest"))
SI=(P*T*R)/100
print("Simple Interest = ",SI)



#3. Area of Circle
r=float(input("Enter the Radius of the Circle = "))
a=(22/7)*r**2
print("Area of Circle is ",a)



#4. Area of Triangle
a = float(input('Enter first side of the triangle '))  
b = float(input('Enter second side of the triangle '))  
c = float(input('Enter third side of the triangle '))   
s = (a + b + c) / 2  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is ',area)   




#5. Celsius to Fahrenheit
c = float(input('Enter temperature in Celsius '))
f=(c*9/5)+32
print("Temperature in Fahrenheit is ",f)



#6. Area of Rectangle
l =float(input(" Enter the Length of the Rectangle "))
b =float(input(" Enter the Breadth of the Rectangle "))
a=l*b
print("The Area of the Rectangle is ",a)




#7. Perimeter of Square
s = float(input("Enter the Side of the Square "))
a=4*s
print("Perimeter of the Square is ",a)




#8. Circumference of a Circle
r = float(input("Enter the Radius of the Circle "))
c = 2*(22/7)*r
print("Circumference of the Circle is ",c)




#9. Swapping of Two Numbers
a=float(input("value of a "))
b=float(input("value of b "))
temp,a=a,b
b=temp
print("The Value of a after Swapping = ",a)
print("The Value of b after Swapping = ",b)

