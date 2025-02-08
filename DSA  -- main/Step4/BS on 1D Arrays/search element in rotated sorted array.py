arr=[4,5,6,7,0,1,2,3]
target=0

n=len(arr)

ans=-1
low=0
high=n-1

while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        ans=mid
    if arr[mid]>=arr[low]:
        if arr[low]<=target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        if arr[mid]<target<=arr[high]:
            low=mid+1
        else:
            high=mid-1
print(ans)
