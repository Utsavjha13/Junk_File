s=input("write a string :")
b=s.split(" ")
l=[]
for i in b:
    l.append(i[::-1])
print(" ".join(l))