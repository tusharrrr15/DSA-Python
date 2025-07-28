def freq_map(n):
    nums = n
    f = dict()
    for i in range(0,len(nums)):
        if nums[i] in f:
            f[nums[i]] += 1
        else:
            f[nums[i]] = 1
    return f
n = [1,2,3,1,1,2,4,5,6,3,2,7]
res = freq_map(n)
print(res)