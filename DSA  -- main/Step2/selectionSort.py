def sortArray(arr):
    n=len(arr)
    for i in range(n):
        ind=i
        for j in range(i+1,n):
            if arr[j]<arr[ind]:
                ind=j

        arr[i],arr[ind]=arr[ind],arr[i]

    return(arr)

if __name__ == "__main__":
    arr=[13,46,24,52,20,9]
    print(sortArray(arr))
