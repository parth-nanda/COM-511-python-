#3. Write a Python program to take an email address and print the domain name.
email=input("Enter Email:")
index=email.find("@")
domain=email[index+1:]
print("Domain=",domain)
