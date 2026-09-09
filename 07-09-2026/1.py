# write a Python program to simulate a digital lock system.

# The lock should ask the user to enter a 4-digit PIN.If the entered PIN does
# not contain exactly 4 digits,the program should display an error message and ask again.
# If the entered PIN is correct,the lock should open.Otherwise,the program should 
# ask the user to try again.
correct_pin="2580"
while True:
    pin=input("enter 4 digit pin number:")
    if len(pin)!=4:
        print("PIN must be exactly 4 digits.")
        continue
    if pin ==correct_pin:
        print("Lock opened.")
        break
    else:
        print("Wrong pin . try again")