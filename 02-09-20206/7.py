#12. Write a Python program to take a password and check whether it contains @
# and has at least 8 charcters.
password = input("Enter Password: ")
print("@" in password and len(password) >= 8)
