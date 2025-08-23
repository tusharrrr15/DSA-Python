def linear_search(arr,target):
    n=len(arr)
    for i in range(0,n):
        if arr[i]==target:
            return i
    return -1

arr=[5,3,2,5,6,7,10,1]
res=linear_search(arr,5)
print(res)
res=linear_search(arr,100)
print(res)
