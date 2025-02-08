str1="(()())(())(()(()))"

ans=""
cnt=0

for i in str1:
    if i=="(":
        if cnt:
            ans+=i
        cnt+=1
    else:
        cnt-=1
        if cnt:
            ans+=i

print(ans)
