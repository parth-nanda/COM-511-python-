# 3.Write a Python program to input numbers in a list and find the second
# largest number.
n = list(map(int,input("Enter numbers:").split()))

n.sort()
n.reverse()

print("Second largest number:", n[1])