# Bubble sort Algorithm to sort values in descending order
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        #print 'I value', arr[i]
        for j in range(len(arr) - 1, 0, -1):
            #print 'J value', arr[j]
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

# main function
arr = [4,2,1,3,5,4,1,4,6,8,9,3,65,34,7,2,7657,3,7,90,3,1,0]
bubble_sort(arr)
print(arr)