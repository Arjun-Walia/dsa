arr=[1,0,1,1,1]
target=0

n=len(arr)

ans=False
low=0
high=n-1

while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        ans=True
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
