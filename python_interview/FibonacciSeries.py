n=int(input("enter the no: "))
l=[0,1]
for i in range(n):
    l.append(l[-1]+l[-2])
print(l)