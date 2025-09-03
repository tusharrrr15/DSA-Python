#Brute Force
# def max_sub(arr):
#     n=len(arr)
#     maxi=float("-inf")
    
#     for i in range(0,n):
#         total = 0
#         for j in range(i,n):
#             total = total + arr[j]
#             maxi = max(maxi,total)
#     return maxi

# arr=[-2,1,-3,4,-1,2,1,-5,4]
# res=max_sub(arr)
# print(res)

#Optimal - Kadane's Algorithm
def max_sub(arr):
    n=len(arr)
    maxi=float("-inf")
    total=0
    for i in range(0,n):
        total=total+arr[i]
        maxi=max(maxi,total)
        
        if total<0:
            total=0
    return maxi

arr=[-2,1,-3,4,-1,2,1,-5,4]
res=max_sub(arr)
print(res)


