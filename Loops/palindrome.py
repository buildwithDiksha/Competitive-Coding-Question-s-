num = int(input("Enter a number : "))
reverse = 0
original_num = num
while num>0:
    digits = num%10
    reverse=reverse*10+digits
    num = num//10
if (reverse==original_num):
    print("palindrome number")
else:
    print("not a palindrome number")    