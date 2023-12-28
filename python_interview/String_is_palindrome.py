def stringpalindrome():
    b=input("give a text: ")
    a=b.replace(" ","").lower()
    if a==a[::-1]:
        print(b +' is pallindrom')
    else:
        print(b +" is Not pallindrom")

stringpalindrome()