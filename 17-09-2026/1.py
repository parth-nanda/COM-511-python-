#5.Write a python progrsm to input numbers in a list and create two separate
#lists for even and odd numbers.
n=list(map(int,input("Enter Number:").split()))
even=[]
odd=[]
for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even Numbers:",even)
print("Odd Numbers:",odd)

    