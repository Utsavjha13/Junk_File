n=str(input("Input the string: "))
rev_word=str(input("enter the word: "))
l=n.split(" ")
for i in range (len(l)):
    if l[i]==rev_word:
        l[i]=l[i][::-1]
print(" ".join(l))
k=[]
for i in range(len(l)):
    if i%2!=0:
        k.append(l[i])
print(k)