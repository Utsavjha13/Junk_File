n=eval(input("Enter array :"))
s="".join(n)
r=s[::-1]
l=[]
for i in r:
    l.append(i)
print(l)