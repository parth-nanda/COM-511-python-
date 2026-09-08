
# 5. Take a password and check length,presence of @, and whether first and last 
# characters are different. 
password=input("Enter Password:")
print("Length at least 8:",len(password)>=8)
print("contains @:","@" in password)
print("First and last different:",password[0]!=password[-1])
