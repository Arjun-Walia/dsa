n=36

low=1
high=n

while low<=high:
    mid=(low+high)//2
    val=mid*mid
    if val<=n:
        low=mid+1
    else:
        high=mid-1

print(high)
