#Brute-Force Solution
# def sec_large(nums):
#     nums.sort()
#     n=len(nums)
#     return nums[n-2]

# nums = [32,55,26,89,77,34]
# res = sec_large(nums)
# print(res)

#Better Solution
# def sec_large(nums):
#     largest = float("-inf")
#     s_largest=float("-inf")
#     n = len(nums)
    
#     for i in range(0,n):
#         largest = max(largest,nums[i])
#     for i in range(0,n):
#         if nums[i]>s_largest and nums[i]<largest:
#             s_largest = nums[i]
#     return s_largest

# nums = [32,55,26,89,77,34]
# res = sec_large(nums)
# print(res)

#Optimal Solution
def sec_large(nums):
    largest = float("-inf")
    s_largest=float("-inf")
    n = len(nums)
    
    for i in range(0,n):
        if nums[i]>largest:
            s_largest=largest
            largest=nums[i]
        elif nums[i]>s_largest and nums[i]!=largest:
            s_largest = nums[i]
    return s_largest

nums = [-32,-55,26,-89,-77,-34]
res = sec_large(nums)
print(res)

    