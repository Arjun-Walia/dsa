def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

def qs(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        qs(arr, low, pi - 1)
        qs(arr, pi + 1, high)

if __name__ == "__main__":
    arr = [4, 3, 1, 5, 2, 6, 9, 7]
    low = 0
    high = len(arr) - 1
    qs(arr, low, high)
    print(arr)
