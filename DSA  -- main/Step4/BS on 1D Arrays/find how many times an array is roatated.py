arr = [4,5,6,7,0,1,2,3]

n=len(arr)

low=0
high=n-1
ans=float("inf")
index=-1

while low<=high:
    mid=(low+high)//2
    if arr[low]<=arr[high]:
        if arr[low]<ans:
            index=low
            ans=arr[low]
        break
    if arr[low]<=arr[mid]:
        if ans>arr[low]:
            index=low
            ans=arr[low]
        low=mid+1
    else:
        if ans>arr[mid]:
            index=mid
            ans=arr[mid]
        high=mid-1
print(index)
