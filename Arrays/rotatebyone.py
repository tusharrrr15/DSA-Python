#using slicing
# def rotatebyone(arr):
#     n=len(arr)
#     arr[:] = [arr[n-1]]+arr[0:n-1]
#     return arr

# arr=[5,2,3,9,0,6]
# res=rotatebyone(arr)
# print(res)

#without slicing
def rotatebyone(arr):
    n=len(arr)
    temp=arr[n-1]
    
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
    return arr

arr=[5,2,3,9,0,6]
res=rotatebyone(arr)
print(res)
