
def sortArr(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1

    while left<=mid and right<=high:
        if arr[left]<=arr[right]:    
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    while left<=right:
        temp.append(arr[left])
        left+=1
    
    while mid<=high:
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i]==temp[i-low]

    
def mergeSort(arr,low,high):
    
    if low>=high:
        return
    mid=(high+low)//2


    


















if __name__=="__main__":
    arr=[9, 4, 7, 6, 3, 1, 5]
    n=len(arr)
    print(mergeSort(arr,0,n-1))
