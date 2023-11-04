

print("Choose a math operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")


operation = int(input("Enter the number of your choice: "))




a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))


if operation==1:
    sum=a+b;
elif operation==2:
    sum=a-b;
else:
    sum=a/b;

print(' Result of your Operation  =',sum)