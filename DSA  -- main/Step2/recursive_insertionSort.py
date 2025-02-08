def insertionSort(arr,i,n):
    if i==n:
        return arr
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
    return insertionSort(arr,i+1,n)

arr=[13, 46, 24, 52, 20, 9]
print(insertionSort(arr,0,len(arr)))
