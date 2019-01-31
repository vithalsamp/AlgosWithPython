# Bubble sort in Python
def bubble_sort(arr):
    for i in range(0, len(arr)):
        key1 = arr[i]
        for j in range(0, len(arr)-i-1):
            key2 = arr[j+1]
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# main function
arr = [4,2,1,3,5,4,1]
bubble_sort(arr)
print(arr)