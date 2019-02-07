# Program to find max crsossing subarray in given array
def find_max_crossing_subarray(arr, low, mid, high):
    # max sum in LEFT subarray
    left_sum = -9999999999999999
    sum = 0
    for i in range(mid, 0, -1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    # max sum in RIGHT subarray
    right_sum = -9999999999999999
    sum = 0
    for j in range(mid+1, len(arr)):
        sum = sum + arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


arr = [1, -2, -4, 7, -2, -3, -4, 5, -16, 7, -86, -8, 6, -7, 76, 8]
a,b,c = find_max_crossing_subarray(arr, 0, len(arr)/2, len(arr))
print a, b, c
