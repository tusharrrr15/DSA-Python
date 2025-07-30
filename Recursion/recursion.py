#print x, N times using recursion
# def func(x,N):
#     if N == 0:
#         return
#     print(x)
#     func(x,N-1)
# func(15,3)

#1 to N using Head 
# def func(x,N):
#     if x > N:
#         return
#     print(x)
#     func(x+1,N)
# func(1,5)

# N to 1 using head
# def func(N):
#     if N == 0:
#         return
#     print(N)
#     func(N-1)
# func(5)

# N to 1 using Tail
# def func(x,N):
#     if x>N:
#         return
#     func(x+1,N)
#     print(x)
    
# func(1,5)

# 1 to N using Tail
def func(x,N):
    if N==0:
        return
    func(x+1,N-1)
    print(N)
    
func(1,5)



