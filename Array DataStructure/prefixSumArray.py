"""
PreFix Sum Array
    Can be used in contiguous segments of array.
    A[] =    6  3  -2  4  -1  0  -5
    pre[] =  6  9  7  11  10  10 5
Time Complexity:- O(n) for making pre[] and o(1) to take desired sum.

Constraints:-
    0 <= i <= j <= len(arr) 
How to take out Desired Sum of subarray[i,j]?
if i == 0:
    sum(i,j) = L[j]
else:
    sum(i,j) = L[j] - L[i-1]

"""

def preFixSum(arr):
    a = []
    arr_sum = 0
    for i in range(len(arr)):
        arr_sum += arr[i]
        a.append(arr_sum)
    # print(a)    ---> check the prefix sum array
    return a

print("Enter the array: ")
l = list(map(int, input().split()))

print("Enter the starting and ending index of the array whose sum is to be taken: ")
(i,j) = map(int, input().split())
a = preFixSum(l)
try:
    if(i==0):
        result = a[j]
    else:
        result = a[j] - a[i-1]

    print("The sum of the subarray is", result)

except Exception as e:
    print(e)