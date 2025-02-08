arr=[3, 4, 6, 7, 9, 12, 16, 17]
target=6

#iterative code

n=len(arr)
low=0
high=n-1

while low<=high:
    mid = (low+high)//2
    if target==arr[mid]:
        print(mid)
        break
    elif target<arr[mid]:
        high=mid-1
    else:
        low=mid+1


#recursive code

def binarySearch(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binarySearch(arr,mid+1,high,target)
    return binarySearch(arr,low,mid-1,target)

def search(nums, target):
    return binarySearch(nums, 0, len(nums) - 1, target)

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    ind = search(a, target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind) 
    
