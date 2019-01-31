# Implement original Merge sort algorithms
def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r- q

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[p + i]

    for j in range(0, n2):
        R[j] = arr[q + 1 + j]

    # Merge the temp L and R arrays back into arr[p..r]
    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted
def merge_sort(arr,p,r):
    if p < r:

        q = ((p+r))//2

        # Sort first and second halves
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


# Main program
arr = [10, 30, 1, 34, 54, 63, 5, 6, 7, 3]

merge_sort(arr, 0, len(arr)-1)

print("\nSorted array is")
for i in range(len(arr)):
    print("%d" %arr[i]),