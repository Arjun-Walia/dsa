arr=[11,33,33,11,33,11]
n=len(arr)

#better approach

dic={}

for i in arr:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

for i in dic:
    if dic[i]>n//3:
        print(i)

#optimal code

cnt1=0
cnt2=0
el1=float("-inf")
el2=float("-inf")

for i in range(n):
    if cnt1==0 and arr[i]!=el2:
        cnt1=1
        el1=arr[i]
    elif cnt2==0 and arr[i]!=el1:
        cnt2=1
        el2=arr[i]
    elif arr[i]==el1:
        cnt1+=1
    elif arr[i]==el2:
        cnt2+=1
    else:
        cnt1-=1
        cnt2-=1
    
print(el1,el2)
