#3. Write a Python program to detect double space in a string.
t=input("Enter a string:")
#print(" " in t)
print(t.find(" "))


#4. Write a Python program to replace double spaces from problem 3 with single spaces.
t=input("Enter a string:")
t=t.replace("  "," ")
print(t)