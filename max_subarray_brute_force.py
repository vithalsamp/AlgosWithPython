# Identify max subarray using Brute force

def max_subarray_brute_force(arr):
     max_sum = -99999999999
     for i in range(0, len(arr)):
         sum = 0
         for j in range(i, len(arr)):
             sum = sum + arr[j]
             if sum > max_sum:
                 max_sum = sum
                 low = i
                 high = j
     return low, high, max_sum


# Main program
#arr = [-2, -5, 6, -2, -3, 1, 5, -6]
arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
a, b, c = max_subarray_brute_force(arr)
print(a, b, c)