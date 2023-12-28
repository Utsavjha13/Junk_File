def listcompare(l1,l2):
    if len(l1)!=len(l2):
        return False
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            return False
    return True
l1=[2,5,6,7,9,12,76,2,28,999,26]
l2=[2,5,6,7,9,12,76,2,28,999,26,65]
print(listcompare(l1,l2))