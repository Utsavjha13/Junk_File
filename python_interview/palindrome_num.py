n = int(input("enter the num: "))
temp = n
new_num = 0
while (n > 0):
    r = n % 10
    n = n // 10
    new_num = new_num * 10 + r

if new_num == temp:
    print("palindrome")