def is_palindrome(num):
    return str(num) == str(num)[::-1]
n = int(input("enter a number :"))

if is_palindrome(n):
    print("Palindromr Number")
else:
    print("Not a Palindrome Number")
