def movezeros(arr,n):
    j=-1
    for i in range(n):
        if arr[i]==0:
            j=1
            break
    if j==-1:
        return arr

    for i in range(j+1,n):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1

    return arr

if __name__ == "__main__":
    arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    n=len(arr)
    res=movezeros(arr,n)
    print(res)
    
