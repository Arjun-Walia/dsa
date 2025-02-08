arr= [3,3,4]

#better code

Map={}

for i in arr:
    if i not in Map:
        Map[i]=1
    else:
        Map[i]+=1
    
print(max(Map, key=Map.get))

#optimal code

el=arr[0]
cnt=0

for i in range(len(arr)):
    if cnt==0:
        el=arr[i]
        cnt=1
    elif el==arr[i]:
        cnt+=1
    else:
        cnt-=1

cnt1=0

for i in arr:
    if i==el:
        cnt1+=1

if cnt1>len(arr)//2:
    print(el)
