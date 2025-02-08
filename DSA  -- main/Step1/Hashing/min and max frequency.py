def frequency(arr,n):
    mp={}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    maxF=max(mp.values())
    minF=min(mp.values())
    maxE = [key for key, value in mp.items() if value == maxF]
    minE = [key for key, value in mp.items() if value == minF]
    print(maxE,minE)
    
if __name__=="__main__":
    arr = [10, 5, 10, 15, 10, 5]
    n=len(arr)
    frequency(arr,n)
