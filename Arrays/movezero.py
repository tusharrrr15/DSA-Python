#Brute Force
# def movezero(arr):
#     n=len(arr)
#     temp=[]
#     for i in range(0,n):
#         if arr[i]!=0:
#             temp.append(arr[i])
#     nz=len(temp)
#     for i in range(0,nz):
#         arr[i]=temp[i]
#     for i in range(nz,n):
#         arr[i]=0
#     return arr

# nums=[1,0,2,4,3,0,0,3,5,1]
# res=movezero(nums)
# print(res)

#Optimal Solution
def movezero(arr):
    n=len(arr)
    if n==1:
        return
    i=0
    while i<n:
        if arr[i]==0:
            break
        i+=1
    if i==n:
        return
    j=i+1
    while j<n:
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    return arr

nums=[1,0,2,4,3,0,0,3,5,1]
res=movezero(nums)
print(res)