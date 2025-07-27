def countDigit(n):
    num = n
    count = 0
    while num>0:
        count += 1
        num = num//10
    return count

n = int(input())
res = countDigit(n)
print(res)

