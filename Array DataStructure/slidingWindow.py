"""
Implementation of Maximum Sum Subarray of size K
    Input:-  2  1  5  1  3  2,   k = 3
    Output:- 9
    Input:-  1  9  -1  -2  7  3  -1  2,  k = 4
    Output:- 13

Sliding Window Technique:-
    1. Take a k-size window, and initialize (wSum-->WindowSum and mSum-->MaxSum) to 0.
    2. Take the wSum and store max(wSum, mSum) to mSum.
    3. Slide the window from start to end.

"""
# Problem:- Given an array of integers n and a positive number k, find the maximum sum of any
#           contiguous subarray of size K.
# Constraints:-
#     0 < k =< n

def maxSum(arr, n, k):
    wSum = 0
    mSum = 0
    # calculating the window sum
    for i in range(k):
        wSum += arr[i]
    
    # storing the first wSum to mSum
    mSum = wSum
    
    #sliding the window to the end to the arr
    for i in range(k, n):
        wSum = wSum + arr[i] - arr[i-k]
        mSum = max(wSum, mSum)
    
    return mSum


print("Enter the elements of array: ")
l = list(map(int, input().split()))

print("Enter the size of subarray: ")
k = int(input())

n = len(l)

result = maxSum(l, n, k)

print("The maximum sum of the subarray of size", k, "is", result)