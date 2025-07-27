def factor(num):
    result = []
    for i in range(1,num//2):
        if num%i == 0:
            result.append(i)
    result.append(num)
    return result
num = int(input())
factors = factor(num)
print(factors)

    