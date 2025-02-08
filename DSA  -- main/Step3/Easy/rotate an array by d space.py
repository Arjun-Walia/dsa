arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

n = len(arr)
k = k % n
temp = arr[-k:]
for i in range(n - k - 1, -1, -1):
    arr[i + k] = arr[i]
for i in range(k):
    arr[i] = temp[i]

print(arr)

