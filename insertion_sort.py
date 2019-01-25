# Insertion sort Algorithm in Python
def insertion_sort(arr):
    for i in range(1,len(arr)):
        # previous value from array list
        key = arr[i]

        # Next value form array list
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
        #print arr

arr = [4,2,1,3,5,4,1]
insertion_sort(arr)
print arr
