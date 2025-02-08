arr=[1,3,5,6]
x=2

n=len(arr)

low=0
high=n-1

while low<=high:
    mid = (low+high)//2
    if x==arr[mid]:
        print(mid)
        break
    elif x<arr[mid]:
        high=mid-1
    else:
        low=mid+1
print(low)     
