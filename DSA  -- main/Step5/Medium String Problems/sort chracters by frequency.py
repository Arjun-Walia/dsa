str1 = "Aabb"
mp = {}

for i in str1:
    if i in mp:
        mp[i] += 1
    else:
        mp[i] = 1

ans = ""
sorted_items = sorted(mp.items(), key=lambda x: (-x[1], x[0]))
for key, value in sorted_items:
    ans += key * value

print(ans)
