# 2.Write a python program to take a 2-digit number as input and print the sum of its digits.
# Example:57=5+7=12

n = int(input("Enter a 2-digit number : "))

first = n // 10
sec = n % 10

print(f"Sum of 2-digits numbers : {first + sec}")
