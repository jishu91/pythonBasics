
#  using if-else statement 
# Input: a = 2, b = 4
# Output: 4

# Input: a = -1, b = -4
# Output: -1

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# if num1 >= num2:
#     print(num1)
# else:
#     print(num2)

# show using function
def max(a,b):
    if a >= b:
        return a
    else:
        return b
# intilize variable
a = 20
b = 20
print(max(a,b))

# Using max() function
a = 5 
b = 90
maximum = max(a,b)
print(maximum)

# Using Ternary Operator
a = 500 
b = 890
print(a if a>=b else b)

#  Using sort() method
a = 200 
b = 30
x=[a,b]
x.sort()
print(x[-1])