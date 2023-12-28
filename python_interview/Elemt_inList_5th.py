# Write a Python program that accepts a list of integers and calculates the length and the fifth element.
# Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

def listcount(l1):
    a=len(l1)
    b=l1[4]
    if a==8 and l1.count(b)==3:
        return True
    else:
        return False

l1=eval(input("Enter the list : "))
print(listcount(l1))