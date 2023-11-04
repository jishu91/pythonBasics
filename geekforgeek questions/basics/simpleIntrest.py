# Input : P = 10000
#         R = 5
#         T = 5
# Output :2500.0
# We need to find simple interest on 
# Rs. 10,000 at the rate of 5% for 5 
# units of time.

def simple_intrest(p,r,t):
    print("The principal is ",p)
    print("The time period is ",t)
    print("The rate of intrest is ",r)      

    si = (p * t * r)/100

    print('The simple intrest is :',si)
    # return si
# simple_intrest(8,6,8)        

# with Taking input from user
P = int(input("Enter the principal amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of intrest :"))
simple_intrest(P,T,R)  