array = [2, 3, 4, 1, 2]

def reverse(f, l):
    if f >= l:
        return array
    array[f], array[l] = array[l], array[f]
    return reverse(f + 1, l - 1)

print(reverse(0, len(array) - 1))
