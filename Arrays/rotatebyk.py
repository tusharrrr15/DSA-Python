#Brute Force
# def rotatebyk(arr,k):
#     n=len(arr)
#     k=k%n
    
#     for i in range(0,k):
#         temp=arr[n-1]
#         for j in range(n-2,-1,-1):
#             arr[j+1]=arr[j]
#         arr[0]=temp
#     return arr

# arr=[3,9,5,6,7,2]
# res=rotatebyk(arr,3)
# print(res)

# def rotatebyk(arr,k):
#     n=len(arr)
#     k=k%n
    
#     for i in range(0,k):
#         temp=arr.pop()
#         arr.insert(0,temp)
              
#     return arr

# arr=[3,9,5,6,7,2]
# res=rotatebyk(arr,9)
# print(res)

#Better Solution
# def rotatebyk(arr,k):
#     n=len(arr)
#     k=k%n
    
#     arr[:]=arr[n-k:]+arr[:n-k]
#     return arr

# arr=[3,9,5,6,7,2,8]
# res=rotatebyk(arr,9)
# print(res)

#Optimal solution

def reverse(arr,left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    

arr=[3,9,5,6,7,2,8]
k=3
n=len(arr)
reverse(arr,n-k,n-1)
reverse(arr,0,n-k-1)
reverse(arr,0,n-1)
print(arr)




    
    