s = "anagram"
t = "nagaram"

#better code

mp1 = {}
mp2 = {}

for i in s:
    if i in mp1:
        mp1[i] += 1
    else:
        mp1[i] = 1

for i in t:
    if i in mp2:
        mp2[i] += 1
    else:
        mp2[i] = 1

print(sorted(mp1.items()) == sorted(mp2.items()))


#optimized code

if len(s)!=len(t):
        print(False)
else:
    mp={}
    for i in s:
        if i in mp:
            mp[i]+=1
        else:
            mp[i]=1
    
    for i in t:
        if i in mp:
            mp[i]-=1
        else:
            print(False)
            break
    else:
        if all(val==0 for val in mp.values()):
            print(True)
        else:
            print(False)
