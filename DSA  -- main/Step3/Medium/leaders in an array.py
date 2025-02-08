arr=[10,22,12,0,3,5]
ans=[]
maxi=float("-inf")
n=len(arr)
for i in range(n-1,-1,-1):
    if arr[i]>maxi:
        ans.append(arr[i])
    maxi=max(maxi,arr[i])

print(ans[::-1])
