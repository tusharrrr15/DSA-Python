from math import sqrt

def factor(num):
    result = []
    for i in range(1,int(sqrt(num))+1):
        if num%i == 0:
            result.append(i)
            if num//i != i:
                result.append(num//i)
    result.sort()
    return result
num = int(input())
factors = factor(num)
print(factors)
