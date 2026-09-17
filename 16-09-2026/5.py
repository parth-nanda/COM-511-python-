# 4.Write a Pyhton program to input a list of numbers and create a new list containing only
# unique elements.
n=list(map(int,input("Enter Elements:").split()))
new=[]
for i in n:
    if i not in new:
        new.append(i)
print("Unique Elements:",new)