def cubeofnumber(n):
    for i in range(1,n):
        yield i**3
n=int(input("Enter the number: "))
it=cubeofnumber(n)

while True:
    try:
        print(next(it))
    except StopIteration :
        break