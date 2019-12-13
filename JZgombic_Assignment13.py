#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Part I ­ Implement the Fibonnaci Sequence

fib = input("Please enter a positive integer to search the nth Fibonacci Number : ")
gcda = input("Please enter a positive integer as the first number in the GCD Calculation : ")
gcdb = input("Please enter a positive integer as the second number in the GCD Calculation : ")

def Fibonacci(fib):

    if int(fib) < 0: 
        print("Incorrect input") 
    elif int(fib)==1: 
        return 0
    elif int(fib)==2: 
        return 1
    else: 
        return Fibonacci(int(fib)-1)+Fibonacci(int(fib)-2) 

print("")  
print ("The nth Fibonacci number from your input is: ",end="")
print(Fibonacci(int(fib))) 
    

#Part II ­ Implement Euclid’s GCD Algorithm

def euclid(gcda,gcdb):

    if (int(gcdb) == 0):
        return int(gcda) 
    else:
        return euclid(int(gcdb),int(gcda)%int(gcdb))
    
print("")
print ("The gcd of of your input is: ",end="")
print (euclid(int(gcda),int(gcdb)))


#Part III ­ String Comparison

def compareTo(s1, s2): 
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])

print("")
print (compareTo('shortstr', 'longstring'))
print (compareTo('same', 'same'))
print (compareTo('longstring', 'shortstr'))
