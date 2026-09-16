# 12. Write a Python program to print an inverted right-angled triangle using stars.
# * * * *
# * * *
# * *
# *
n=4
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()