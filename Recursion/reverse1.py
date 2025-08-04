#reverse an array using recursion
def func(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    func(arr,left+1,right-1)
    
def reverseArray(arr,l,r):
    func(arr,l,r)
    return arr

arr = [1,2,3,4,5,6]
x = reverseArray(arr,0,len(arr)-1)
print(x)


