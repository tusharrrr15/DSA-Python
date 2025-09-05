#Brute force
# def max_count(arr):
#     n=len(arr)
#     max_count=0
#     for i in range(0,n):
#         num=arr[i]
#         count=1
#         while num+1 in arr:
#             count+=1
#             num=num+1
#         max_count=max(max_count,count)
#     return max_count
        
# arr=[1,99,101,98,2,5,3,100]
# res=max_count(arr)
# print(res)

#Better solution
# def max_count(arr):
#     n=len(arr)
#     arr.sort()
#     last_smaller=float("-inf")
#     longest=0
    
#     for i in range(0,n):
#         num=arr[i]
#         if num-1==last_smaller:
#             count+=1
#             last_smaller=num
#         elif num!=last_smaller:
#             count=1
#             last_smaller=num
#         longest=max(longest,count)
#     return longest
        
        
# arr=[1,99,101,98,2,5,3,100]
# res=max_count(arr)
# print(res)

#optimal
def max_count(arr):
    n=len(arr)
    my_set=set()
    for i in range(0,n):
        my_set.add(arr[i])
    
    longest=0
    count=0
    
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)
    
    return longest
        
        
arr=[1,99,101,98,2,5,3,100,102]
res=max_count(arr)
print(res)