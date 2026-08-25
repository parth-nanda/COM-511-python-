# 3.write a Python program to take an amount in rupees and calculate how many rupees500   and rupees 100 notes are needed.
# Example:3800=7notes of 500 and 3 notes of 100

amt = int(input("Enter an Amount : "))

note_500 = amt // 500
rem_amt = amt % 500
note_100 = rem_amt // 100

print(f"{note_500} Notes of 500 & {note_100} Notes of 100")