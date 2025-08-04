# reverse an array using while loop
arr = [1,2,3,4,5,6]
left = 0
right = len(arr)-1

while True:
    if left>=right:
        break
    arr[left],arr[right] = arr[right],arr[left]
    left += 1
    right -= 1
print(arr)