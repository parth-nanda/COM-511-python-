#14 Write a Python program to print a centereed pyramid using stars.
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
n=4
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
