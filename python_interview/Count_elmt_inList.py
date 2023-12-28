# Write a Python program to find a list of integers with exactly two occurrences of nineteen and
# at least three occurrences of five. Return True otherwise False.

def listpuzz(l1):
    a=l1.count(19)
    b=l1.count(5)
    if a==2 and b>=3:
        return True
    else:
        return False
l1=eval(input("Enter a list : "))
print(listpuzz(l1))
