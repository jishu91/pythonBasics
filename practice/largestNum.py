num1 = float(input("Enter num1 number: "))
num2 = float(input("Enter num2 number: "))
num3 = float(input("Enter num3 number: "))

if num1>num2 and num1>num3:
    print(num1," is the largest")
elif num2>num1 and num2>num3:
    print(num2," is the largest")
else:
    print(num3," is the largest")

