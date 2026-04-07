# 7.Program to find Greatest Common Divisor of two numbers.
#For example, the GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.

a=int(input("enter frist number"))
b=int(input("enter second number"))
for i in range (1,a+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)   