#11. Write  a Python program to print a right-angled triangle using stars.
# *
# * *
# * * *
# * * * *
n=4
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
