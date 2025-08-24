# #Brute Force
# def missing_number(arr):
#     n=len(arr)
#     for i in range(0,n+1):
#         if i not in arr:
#             return i
        
# arr=[0,1,3]
# res=missing_number(arr)
# print(res)

#Better
# def missing_number(arr):
#     n=len(arr)
#     freq={}
    
#     for i in range(0,n+1):
#         freq[i]=0
#     for num in arr:
#         freq[num]=1
#     for k,v in freq.items():
#         if v==0:
#             return k
        
# arr=[0,2,3]
# res=missing_number(arr)
# print(res)

#Optimal solution
# def missing_number(arr):
#     n = len(arr)
#     total = n  
#     expected_sum = total * (total + 1) // 2
#     actual_sum = sum(arr)
#     return expected_sum - actual_sum

# arr = [0, 2, 3]
# res = missing_number(arr)
# print(res) 

#Optimal solution without sum() function
def missing_number(arr):
    n = len(arr) 
    total = n     

    expected_sum = total * (total + 1) // 2
    
    actual_sum = 0
    for i in range(n):
        actual_sum += arr[i]
    
    return expected_sum - actual_sum

arr = [0, 2, 3]
res = missing_number(arr)
print(res)