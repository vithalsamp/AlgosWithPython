# Find max subarray program
import math
#from find_max_crossing_subarray import find_max_crossing_subarray
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


def find_max_subarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    else:
        mid = int(((low + high)/2))
        left_low, left_high, left_sum = find_max_subarray(arr, low, mid)
        right_low, right_high, right_sum = find_max_subarray(arr, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, len(arr)/2, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


# Main program
arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
a, b, c = find_max_subarray(arr, 0, len(arr)-1)
print a, b, c
