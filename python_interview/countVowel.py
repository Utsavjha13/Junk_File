n=input("Enter the world: ")
vowel=0
cons=0
for i in n:
    if i.lower() in "aeiou":
        vowel+=1
    if i.lower() not in "aeiou":
        cons+=1
print("vowel is {} and consonent is {}".format(vowel,cons))

