"""
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’ 
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.
"""

import sys
print("GFC")

# O(n * k) solution for finding
# maximum sum of a subarray of size k

INT_MIN = -sys.maxsize - 1
print(INT_MIN)


def maxSum(arr, n, k):
    # Initialize result
    max_sum = INT_MIN

    # Consider all blocks
    # starting with i.
    for i in range(n-k+1):
        print("i: "+str(i))
        current_sum = 0
        for j in range(k):
            print("j: {}".format(j))
            current_sum = current_sum + arr[i+j]
            print("current_sum: "+str(current_sum))
        # update result if required
        max_sum = max(current_sum, max_sum)
    return max_sum


# Driver code
arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
