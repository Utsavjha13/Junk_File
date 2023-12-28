def findMaxMin(l):
    max_val=min_val=l[0]
    if len(l)==0:
        return None
    for i in l:
        if i>max_val:
            max_val=i
        if i<min_val:
            min_val=i
    return max_val,min_val

list=eval(input("Enter the list: "))
max_num, min_num=findMaxMin(list)
print("{0} is max and {1} is min of the list {2}".format(max_num,min_num,list))