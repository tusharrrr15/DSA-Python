# Parameterized recusrion
# def func(sum,i,N):
#     if i>N:
#         print(sum)
#         return
#     func(sum+i,i+1,N)
# func(0,1,10)

# functional recursion
def func(N):
    if N == 1:
        return 1
    return N + func(N-1)
x = func(5)
print(x)