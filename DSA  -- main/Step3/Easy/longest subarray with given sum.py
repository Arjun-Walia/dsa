#better code

def longestSubarray(arr,k):
    n=len(arr)
    length=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if s==k:
                length=max(length,j-i+1)
    return length

if __name__=="__main__":
    arr=[1,1,-1]
    k=1
    Sub=longestSubarray(arr,k)
    print(Sub)

#optimal code

def getlongestSubarray(arr,k):
    n=len(arr)
    right,left=0,0
    Sum=arr[0]
    length=0
    while right<n:
        while left<=right and Sum>k:
            Sum-=arr[left]
            left+=1

        if Sum==k:
            length = max(length,right-left+1)

        right+=1

        if right<n:
            Sum+=arr[right]

    return length

if __name__=="__main__":
    Sub2=getlongestSubarray(arr,k)
    print(Sub2)
