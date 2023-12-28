n=int(input("Enter the number :"))
for i in range (n//2):
    if i*i==n:
        print("perfect squ")
        break
else:
    print("Not perfect sqr")