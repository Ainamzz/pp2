def is_palindrome(s):
    return s == s[::-1]
txt = input("Enter a string:")
if is_palindrome(txt):
    print("YES")
else:
    print("NO")