str1 = "ecbaddce"
k = 3
mp = {}
maxlen = 0
l = 0

for r in range(len(str1)):
    if str1[r] in mp:
        mp[str1[r]] += 1
    else:
        mp[str1[r]] = 1

    while len(mp) > k:
        mp[str1[l]] -= 1
        if mp[str1[l]] == 0:
            del mp[str1[l]]
        l += 1

    # Only update maxlen if the substring has exactly k distinct characters
    if len(mp) == k:
        maxlen = max(maxlen, r - l + 1)

print(maxlen)  # Output should be 7
