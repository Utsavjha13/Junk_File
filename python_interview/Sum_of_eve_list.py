def sumOfList(l):
    count = 0
    for i in l:
        if i % 2 == 0:
            count += i
    return count


list = eval(input("enter the list: "))
print("Sum of the list is: {}".format(sumOfList(list)))
