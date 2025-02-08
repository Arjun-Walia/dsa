s = "aabcb"

ans=0

for i in range(len(s)):
    freq={}
    for j in range(i,len(s)):
        if s[j] in freq:
            freq[s[j]]+=1
        else:
            freq[s[j]]=1

        if len(freq)>1:
            ans+=max(freq.values())-min(freq.values())

print(ans)
        
