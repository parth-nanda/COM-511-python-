# 5. Write a Python program to input marks of 5 students.
# For each student,the program should check whether the entered marksare valid 
# or invalid.Marks are considered valid only if they are between 0 and 100.If the marks 
# are invalid,the program should display"Invalid Marks skipped" and move to the nextstudent 
# without printing those marks.
for i in range(1,6):
    marks=int(input("Enter marks:"))

    if marks<0 or marks>100:
        print("Invalid marks skipped")
        continue
    print("Valid marks:",marks)