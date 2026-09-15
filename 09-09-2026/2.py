# 7.Write a Python Program to detect whether a comment is spam or not.A 
# comment should be treated as spam if it contains any of these keyboards:
# "make a lot of money","buy now","subscribe this", or "click this".
comment=input("Enter comment:")
comment=comment.lower()
if "make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment:
    print("Spam")
else:
    print("Not Spam")