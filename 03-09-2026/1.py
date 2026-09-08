# 1. Take student full name and roll number.Generate email using first 3 letters of first
# name,first 3 letters of last name,and last 3 characters of roll number.
first_name=input("Enter First Name:")
last_name=input("Enter Last Name:")
roll=input("Enter Roll Number:")
email=first_name[:3]+last_name[:3]+roll[-3:]
print(email)



