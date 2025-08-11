def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2,-1,-1):
        is_swap = False
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap = True
        if is_swap == False:
            break 
    return nums

nums = [5,7,8,4,1,6,9,2]
res = bubble_sort(nums)
print("After Sorting: ",res)