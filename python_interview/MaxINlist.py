n=eval(input("enter the array: "))
larger = n[0]
for i in range(1,len(n)):
    if larger<n[i]:
        larger=n[i]
print(larger)