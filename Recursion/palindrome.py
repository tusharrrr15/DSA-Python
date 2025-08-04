# check the given string is palindrome or not using loop
# s = input()
# n = len(s)
# left = 0
# right = n - 1

# is_palindrome = True

# while left < right:
#     if s[left] != s[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1

# if is_palindrome:
#     print("True")
# else:
#     print("False")

# using recursion
def is_palindrome(s,left,right):
    if s[left] != s[right]:
        return False
    if left >= right:
        return True
    return is_palindrome(s,left+1,right-1)

s = str(input())
x = is_palindrome(s,0,len(s)-1)
print(x)