def fnc(arr,mid,limit):
    S=0
    for i in arr:
        S+=i/mid
    if S<=limit:
        return 1
    else:
        return 2

arr=[44,22,33,11,1]
limit=5

low=1
high=max(arr)

ans=float("inf")

while low<=high:
    mid=(low+high)//2
    val=fnc(arr,mid,limit)
    if val==1:
        ans=mid
        break
    if val==2:
        high=mid-1
    else:
        low=mid+1
print(ans)
