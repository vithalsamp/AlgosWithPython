# Original Heap sort implementation in Python


# Identify Parent Node
def parent(i):
    return (i-1)//2


# Identify LEFT node
def left(i):
    return 2*i + 1


# Identify RIGHT node
def right(i):
    return 2*i + 2


# Apply max heap property. Parent node of subtree should be larger then child nodes
def max_heapify(arr, n, i):
    heap_size = n
    l = left(i)
    r = right(i)

    if l < heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# Apply min heap property. Parent node of subtree should be smaller then child nodes
def min_heapify(arr, n, i):
    heap_size = n
    l = left(i)
    r = right(i)

    if l < heap_size and arr[l] < arr[i]:
        smallest = l
    else:
        smallest = i

    if r < heap_size and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i] = arr[smallest]
        min_heapify(arr, n, smallest)


def build_max_heap(arr):
    n = len(arr)
    for i in range((len(arr))//2, -1, -1):
        max_heapify(arr, n, i)


def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)


# Main program
arr = [4, 1, 3, 2, 16, 9, 10, 14, 11, 13, 8, 12, 15, 7]
# arr = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

print('Given Array:', arr)
# Heap Sort function
heap_sort(arr)

print('Sorted Array:', arr)
