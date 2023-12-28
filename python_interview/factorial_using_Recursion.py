def factRec(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factRec(n-1)


a=int(input("Input an integer: "))
print("factorial of {0} is {1}".format(a, factRec(a)))