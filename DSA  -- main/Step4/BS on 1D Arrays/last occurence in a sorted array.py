
def index(arr,n,x):
    low=0
    high=n-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            ans=mid
            low=mid+1
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return ans


arr=[3,4,13,13,13,20,40]
x=13
n=len(arr)

print(index(arr,n,x))
