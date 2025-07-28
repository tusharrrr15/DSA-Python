def freq_map(nums):
    n = len(nums)
    hash_map = {}
    for i in range(0,n):
        hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
    return hash_map

nums = [1,2,3,1,1,2,3,4,5,6,3]
res = freq_map(nums)
print(res)