# This program shows how to speed up merge sort using insertion sort
def merge_insertion_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[mid:]
        R = arr[:mid]

        # use merge sort to sort sub arrays
        insertion_sort(L)
        insertion_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key


# main program
arr = [10, 30, 1, 34, 54, 63, 5, 6, 7, 3, 1, 2]

merge_insertion_sort(arr)

print(arr)
