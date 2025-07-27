def check_armstrong(n):
    num = n
    nod = len(str(num))
    total = 0
    while num>0:
        ld = num%10
        total = total + ld**nod
        num = num//10
    return total
n = int(input())
res = check_armstrong(n)
if n == res:
    print("yes")
else:
    print("no")