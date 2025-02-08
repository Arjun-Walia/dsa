arr=[1,1,0,0,1,1,1,0,1,1,1,1]

max1=0
count=0

for i in arr:
    if i==1:
        count+=1
        max1=max(max1,count)
    else:
        count=0

print(max1)
