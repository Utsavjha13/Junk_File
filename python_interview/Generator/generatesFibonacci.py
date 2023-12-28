def genFibo(n):
    x,y=0,1
    for i in range (n):
        yield x
        x,y=y,x+y

n=int(input("Enter the number: "))
it=genFibo(n)
for i in range(n):
    print(next(it), end=",")