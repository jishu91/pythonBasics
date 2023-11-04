# For example factorial of 6 is 6*5*4*3*2*1 which is 720.

# Using Recursive approach
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1)
num=5
print("factorial of ",num,"is :",factorial(num))

# using In-built function 
import math
def factorial(n):
    return(math.factorial(n))
num1=8
print("factorial of ",num1,"is :",factorial(num1))