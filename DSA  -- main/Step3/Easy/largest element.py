arr=[3,1,2,2,5,4]
largest=arr[0]
for i in range(1,len(arr)):
    if arr[i]>largest:
        largest=arr[i]

print(largest)