def genPrime(n):
    for i in range (2, n +1):
        for j in range (2,i):
            if i%j==0:
                break
        else:
            yield i


n=int(input("Enter the number: "))
it=genPrime(n)
for i in it:
    print(i)

