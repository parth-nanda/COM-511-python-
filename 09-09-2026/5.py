#3.Write a Python program to input two numbers and find their greatest common divisor using
# a loop.
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# num1,num2=a,b
# while b!=0:
#     remainder=a%b
#     a=b
#     b=remainder
#     print(f"The GCD of {num1} and {num2} is {a}")


import math

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
gcd=math.gcd(num1,num2)
print(f"The GCD of {num1} and {num2} is {gcd}")