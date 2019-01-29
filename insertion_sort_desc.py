# Insertion sort Algorithm in Python -  Sort Value sin descending order
def insertion_sort(arr):
    for i in range(1,len(arr)):
        # previous value from array list
        key = arr[i]

        # Next value form array list
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

arr = [31, 41, 59, 26, 41, 58]
insertion_sort(arr)
print(arr)
