# factorial of number
def fact(N):
    if N == 0 or N == 1:
        return 1
    return N*fact(N-1)

x = fact(5)
print(x)