import random


def randomNumGen(a,b):
    while True:
        yield random.randrange(a,b)

a=int(input("enter the 1st number: "))
b=int(input("enter the 2nd number: "))
it=randomNumGen(a,b)
for i in range(10):
    print(next(it))