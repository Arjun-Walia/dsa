array = [1, 2, 1, 3, 2]
queries = [1, 3, 4, 2, 10]

dic = {}
for i in array:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

results = []
for j in queries:
    if j in dic:
        results.append(dic[j])
    else:
        results.append(0)

print(results)
