arr=[2, 4, 6, 8, 8, 8, 11, 13]
x=8

n=len(arr)

low=0
high=n-1

ans=-1

while low<=high:
    mid=(low+high)//2
    if arr[mid]<=x:
        low=mid+1
    else:
        high=mid-1
    if arr[mid]==x:
        ans=mid


ans2=-1

low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]>=x:
        high=mid-1
    else:
        low=mid+1 
    if arr[mid]==x:
        ans2=mid
        low=mid+1


print(ans-ans2+1)
