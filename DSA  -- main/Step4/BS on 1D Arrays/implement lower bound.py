arr=[3,5,8,15,19]
target=20

n=len(arr)

low=0
high=n-1

ans=float("-inf")

while low<=high:
    mid=(low+high)//2
    if arr[mid]>=target:
        ans=mid
        high=mid-1
    else:
        low=mid+1

print(ans)
