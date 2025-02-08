arr=[2,1,4,7,7,5]

#Better Solution

smallest=arr[0]

for i in range(1,len(arr)):
    if arr[i]<smallest:
        smallest=arr[i]

secondSmallest=10**8

for i in range(0,len(arr)):
    if arr[i]!=smallest and arr[i]<secondSmallest:
        secondSmallest=arr[i]

#Optimal Solution

Smallest=arr[0]
sSmallest=10**8

for i in range(0,len(arr)):
    if arr[i]<Smallest:
        sSmallest=Smallest
        Smallest=arr[i]
    elif arr[i]<Smallest and arr[i]>sSmallest:
        sSmallest=arr[i]

print(sSmallest)
