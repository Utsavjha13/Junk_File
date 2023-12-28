def maxMin(l):
    a=max(l)
    b=min(l)
    return a, b

l=eval(input("Enter the list: "))
print("max {0[0]} and min {0[1]} of the list {1}".format(maxMin(l),l))