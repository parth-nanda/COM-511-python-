# 6. Write a Python program to input four numbers from the user and 
# find the greatest number amoog them.

a,b,c,d=map(int,input("Enter four numbers:").split())
if a>b and a>c and a>d:
    print("A is greater=",a)
elif b>a and b>c and b>d:
    print("B is greater=",b)
elif c>a and c>b and c>d:
    print("C is greater=",c)
else:
    print("D is greatrer=",d)


a,b,c,d=map(int,input("Enter four numbers:").split())
m=max(a,b,c,d)
print("Greatest Number:",m)