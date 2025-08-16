#Brute - Force
# def remove_duplicate(arr):
#     n=len(arr)
#     freq_map={}
#     for i in range(0,n):
#         freq_map[arr[i]]=0
    
#     j=0
#     for k in freq_map:
#         arr[j]=k
#         j+=1
#     return j

# arr=[1,1,1,2,2,3,4,4,5,6]
# res=remove_duplicate(arr)
# print(arr)
# print(res)

#Optimal Solution
def remove_duplicate(arr):
    n=len(arr)
    if n==1:
        return 1
    
    i=0
    j=i+1
    while j<n:
        if arr[j]!=arr[i]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    return i+1

arr=[1,1,1,2,2,3,4,4,5,6]
res=remove_duplicate(arr)
print(arr)
print(res)