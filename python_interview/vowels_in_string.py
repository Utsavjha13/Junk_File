def vowInStr(s):
    vow = "aeiou"
    strng = s.lower()
    count = 0
    for i in strng:
        if i in vow:
            count += 1
    return count


print("number of vowels in the string is: ",vowInStr(input("Give a string: ")))
