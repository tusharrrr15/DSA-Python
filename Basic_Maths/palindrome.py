def check_palindrome(n):
    num = n
    result = 0
    while num>0:
        ld = num%10
        result = result*10 + ld
        num = num//10
    return result
n = int(input())
res = check_palindrome(n)
if res == n:
    print("Yes")
else:
    print("no")
        