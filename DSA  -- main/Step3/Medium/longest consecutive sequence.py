arr=[100,5,4, 200, 1, 3, 2, 4,]

#better code

'''arr=sorted(arr)'''
cnt=0
longest=1
lastsmaller=float("-inf")

for i in arr:
    if i-1==lastsmaller:
        cnt+=1
        lastsmaller=i
    elif i!=lastsmaller:
        cnt=1
        lastsmaller=i
    longest=max(longest,cnt)
print(longest)

#optimal code

c=0
longest=1
st=set()

for i in arr:
    st.add(i)

for i in st:
    if i-1 not in st:
        c=1
        x=i
        while x+1 in st:
            c+=1
            x+=1
        longest = max(longest,c)
print(longest)
