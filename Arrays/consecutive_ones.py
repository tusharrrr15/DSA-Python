def max_ones(arr):
    n=len(arr)
    count=0
    max_count=0
    
    for i in range(0,n):
        if arr[i]==1:
            count+=1
        else:
            if count>max_count:
                max_count=count
            count=0
    return max(max_count,count)

arr=[1,1,0,1,0,1,1,0,1,1,1,1,1]
res=max_ones(arr)
print(res)