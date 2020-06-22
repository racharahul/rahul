#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.Write a program in python to check whether a person is eligible for voting or not using if-else

age=int(input("enter age : "))
if age >= 18 :
    print("eligible to vote")
else:
    print("not eligible to vote")


# In[4]:


#2.Write a program in python to check whether a number is even or odd using if-else

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("even")
else:
   print("odd")


# In[6]:


#3.Write a program to print the string in reverse order by using string indexing

s=("hello")
a=s[::-1]
print(a)


# In[7]:


#4.Write a python program to check whether a number is positive or not using if-else

num = float(input("Enter a number: "))
if num >= 0:
       print("Positive number")
else:
   print("Negative number")


# In[8]:


#5.Write a python program to find the roots of a quadratic equation using elif

from math import sqrt

print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))     
    x2 = (((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()


# In[9]:


#6.Write  a program in python using nested-if to check whether a number is positive or negative or zero

num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")


# In[10]:


#7.Write a program to accept a number(1-5) and print the given number in words

x=int(input("accept a number "))
if x==1:
  print("ONE")
elif x==2:
  print("TWO")
elif x==3:
  print("THREE")
elif x==4:
    print("FOUR")
elif x==5:
      print("FIVE")
else:
        print("the given number is not in 1-5")


# In[11]:


#8.Write a program in python to read a character and print the given character is vowel or consonant

ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")


# In[ ]:




