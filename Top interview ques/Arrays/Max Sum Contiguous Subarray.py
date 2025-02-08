#Find the contiguous subarray within an array, A of length N which has the largest sum.


def maxSubArray(A):
    maxSum = float('-inf')
    Sum = 0
    
    for i in A:
        Sum += i
        if Sum > maxSum:
            maxSum = Sum
        if Sum < 0:
            Sum = 0
            
    return maxSum