# 2. Take roll number like 2024a1t005 and extract admission year,program code,and roll 
# number digits using slicing.
roll=input("Enter Roll Number:")
print("Admission Year:",roll[:4])
print("Program Code",roll[4:7])
print("Roll Number digits",roll[7:10])