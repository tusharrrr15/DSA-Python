def reverse(n):
    if n<0:
        sign = -1
    else:
        sign = 1
    
    num = abs(n)    
    result = 0
    
    while num>0:
        ld = num%10
        result = result*10 + ld
        num = num//10
    result = result*sign
    return result

n = int(input())
res = reverse(n)
print(res)