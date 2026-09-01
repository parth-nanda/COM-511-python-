# Write a python program to take marks of three subjects out of 100. Print True if the student scored at least 40 in all three subjects and average marks are at least 50.
a,b,c=map(int,input("Enter the marks of three subjects:").split())
if 40 <= a <= 100 and 40 <= b <= 100 and 40 <= c <= 100:
    print("True")
else:
    print("False")