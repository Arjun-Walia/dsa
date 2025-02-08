arr=[2,1,4,7,7,5]

#Better Solution

largest=arr[0]

for i in range(1,len(arr)):
    if arr[i]>largest:
        largest=arr[i]

secondLargest=-1

for i in range(0,len(arr)):
    if arr[i]!=largest and arr[i]>secondLargest:
        secondLargest=arr[i]

#Optimal Solution

Largest=arr[0]
sLargest=-1

for i in range(0,len(arr)):
    if arr[i]>Largest:
        sLargest=Largest
        Largest=arr[i]
    elif arr[i]<Largest and arr[i]>sLargest:
        sLargest=arr[i]

print(sLargest)
