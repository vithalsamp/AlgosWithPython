# Implementing original quick sort algorithm

def quick_sort_partition(arr, p, r):
    x = arr[r]
    i = p-1

    for j in range(p, r):
        if arr[j] <= x:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


# Quick sort Function
def quick_sort(arr, p, r):
    if p < r:
        q = quick_sort_partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)


# Main program
arr = [2, 8, 7, 1, 3, 5, 6, 4]
print('Original Array:', arr)
quick_sort(arr, 0, len(arr)-1)
print('Sorted Array:',arr)