# Import required functions from heap sort script
from heap_sort import build_max_heap, max_heapify, parent


# Return maximum element from heap
def heap_maximum(arr):
    build_max_heap(arr)
    return arr[0]


# Extract maximum element from heap
def heap_extract_max(arr):
    n = len(arr)
    build_max_heap(arr)
    #print n
    if n < 0:
        return 'Heap Underflow'
    max = arr[0]
    arr.remove(max)
    n = len(arr)
    max_heapify(arr, n, 0)
    return max


# Increase key in Heap
def heap_increase_key(arr, i, key):
    build_max_heap(arr)
    if key < arr[i]:
        print('New key is smaller then current key')
    arr[i] = key
    while i > 0 and arr[parent(i)] < arr[i]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)


# Insert element to max heap
def max_heap_insert(arr, key):
    build_max_heap(arr)
    n = len(arr)
    arr.append(-9999999)
    heap_increase_key(arr, n, key)

# arr = [4, 1, 3, 2, 16, 9, 10, 14, 11, 13, 8, 12, 15, 7]
arr = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
# for i in range(len(arr)-1):
#     max_val = heap_extract_max(arr)
#     print(max_val)
build_max_heap(arr)
print(arr)
#heap_increase_key(arr, 8, 15)
max_heap_insert(arr, 10)
print(arr)
