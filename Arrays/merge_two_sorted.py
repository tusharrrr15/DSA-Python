def merge_two_sorted(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    result=[]
    i=0
    j=0
    while i<n and j<m:
        if arr1[i]<=arr2[j]:
            if len(result)==0 or result[-1]!=arr1[i]:
                result.append(arr1[i])
            i+=1
        else:
            if len(result)==0 or result[-1]!=arr2[j]:
                result.append(arr2[j])
            j+=1
            
    while i<n:
        if len(result)==0 or result[-1]!=arr1[i]:
            result.append(arr1[i])
        i+=1
    
    while j<m:
        if len(result)==0 or result[-1]!=arr2[j]:
            result.append(arr2[j])
        j+=1
    return result

arr1=[1,1,1,2,4,6,7]
arr2=[1,2,3,6,7,8,9,10]
res=merge_two_sorted(arr1,arr2)
print(res)
        