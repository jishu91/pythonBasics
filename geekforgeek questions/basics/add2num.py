# Input: num1 = 5, num2 = 3
# Output: 8
# Input: num1 = 13, num2 = 6
# Output: 19

# num1 = int(input("Enter 1st num: "))
# num2 = int(input("Enter 2st num: "))
# sum = num1 + num2
# print(sum)

# Defining add function and returning the result
#To define a function that take two integers 
def add(a,b):
# and return the sum of those two numbers
    return a+b
#initializing the variables
num1 = 2
num2 = 3
#function calling and store the result into sum
sum = add(num1,num2)
print("Defining add function and returning the result:", sum)

# Add two numbers in Python using operator.add() method
num3 = 30
num4 = 10
# adding two nums
import operator
su = operator.add(num3,num4)
print("using operator.add() method:",su)