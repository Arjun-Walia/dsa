arr=[-1,0,1,2,-1,-4]
n=len(arr)
arr=sorted(arr)
ans= []
for i in range(n):
    if i!=0 and arr[i]==arr[i-1]:
        continue
    j=i+1
    k=n-1

    while j<k:
        Sum=arr[i]+arr[j]+arr[k]
        if Sum>0:
            k-=1
        elif Sum<0:
            j+=1
        else:
            temp=[arr[i],arr[j],arr[k]]
            ans.append(temp)
            j+=1
            k-=1

            while j<k and arr[j]==arr[j-1]:
                j+=1
            while j<k and arr[k]==arr[k+1]:
                k-=1
print(ans)
