def median(l):
    d=sorted(l)
    n =len(d)
    if n%2==1:
        mid=d[n//2]
    else:
        median1=d[n//2]
        median2=d[n//2-1]
        mid=(median1+median2)/2
    return mid

list=eval(input("Enter the list: "))
print(median(list))