def frequency(arr,n):
    mp={}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for j in mp:
        print(j,mp[j])


if __name__=="__main__":
    arr = [10, 5, 10, 15, 10, 5]
    n=len(arr)
    frequency(arr,n)
