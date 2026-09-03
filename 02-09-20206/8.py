#13. Write a Python program to take a string and separate characters present at 
# even index positions and odd index positions.

#14. Take an email address and check whether it contains @ and .com
#15. Take a sentence containing double spaces and unwantedd spaces at the
#begining or end.Clean the sentence.
sentence=input("Enter a Sentence")
t=sentence.removeprefix("  "," ")
s=sentence.removesuffix("  "," ")
r=t+s
print(r)