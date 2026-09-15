#8. Write a Python program to repeatedly calculate the sum of digits of a nummber until
#the result becomes a single digit.
#Example:9875---->9+8+7+5=29--->2+9=11--->1+1=2
n = int(input("Enter Number:"))
while n >= 10:
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    n = sum
print("Single Digit:", n)