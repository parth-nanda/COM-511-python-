#2. Write a Python program to take a student name and roll number,then generate a username
#using the first 3 letters of the name and last 2 digits of the roll number.
name=input("Enter Student Name:")
roll=input("Enter Roll No. :")
username=name[0:3]+roll[-2:]
print("Username=",username)