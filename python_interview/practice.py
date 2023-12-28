n=int(input("Enter the number: "))
nw=0
while n>0:
    r=n%10
    n=n//10
    nw=nw*10+r

print(nw)