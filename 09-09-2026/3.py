#1. Write a python program that asks the user to enter a username and password.
# The user should get only 3 attempts.If the correct credentials are entered,display
# "Login Successful" and stop the loop.If all attempts are used,display"Account Locked".

correct_username=input("Enter Correct_Username:")
correct_password=input("Enter Correct_Password:")
attempts=3
while attempts>0:
    username=input("Enter Username:")
    password=input("Enter Password:")

    if username==correct_username and password==correct_password:
        print("Login Successful")
        break
    else:
        attempts=attempts-1
        print("Worng details.Attempts left:",attempts)

    if attempts==0:
        print("Account Locked")



#8. Write a python program to print numbers from 1 to 50, but skip all numbers divisible by 4
