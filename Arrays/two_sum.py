#Brute Force
# def two_sum(arr,target):
#     n=len(arr)
#     for i in range(0,n-1):
#         for j in range(i+1,n):
#             if arr[i]+arr[j] == target:
#                 return [i,j]
            
# arr=[5,9,1,2,4,15,6,3]
# res=two_sum(arr,14)
# print(res)

#Optimal solution
def two_sum(arr,target):
    n=len(arr)
    hash_map={}
    for i in range(0,n):
        remaining=target-arr[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        else:
            hash_map[arr[i]] =i
            
arr=[5,9,1,2,4,15,6,3]
res=two_sum(arr,19)
print(res)