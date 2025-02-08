strs=["dog","racecar","car"]

pre="" 

for i in range(len(strs[0])):
    for s in strs:
        if i==len(s) or s[i]!=strs[0][i]:
            print(pre)
            break
    pre+=strs[0][i]
print(pre)


