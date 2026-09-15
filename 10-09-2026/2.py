#5. Write a Pyhton program to input a number and reverse it using arithmetic operations only.
n=int(input("Enter Number:"))
reverse=0

while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print("Reverse Number:",reverse)
