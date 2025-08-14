def large(nums):
    largest = float("-inf")
    n = len(nums)

    for i in range(0,n):
        largest = max(largest,nums[i])
    return largest

nums = [32,55,26,77,34]
res = large(nums)
print(res)
    