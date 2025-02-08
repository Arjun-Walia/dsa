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
    dict1={}
    maxlen=0
    Sum=0

    for i in range(n):
        Sum+=arr[i]
        if Sum==k:
            maxlen=max(maxlen,i+1)

        rem=Sum-k

        if rem in dict1:
            length=i-dict1[rem]
            maxlen=max(maxlen,length)

        if Sum not in dict1:
            dict1[Sum]=i

    return maxlen


if __name__=="__main__":
    Sub=getlongestSubarray(arr,k)
    print(Sub)
