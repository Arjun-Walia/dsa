s="(1+(2*3)+((8)/4))+1"
cnt=0
maxi=0
for i in s:
    if i=="(":
        cnt+=1
        if cnt>maxi:
            maxi=cnt
    if i==")":
        cnt-=1
print(maxi)
