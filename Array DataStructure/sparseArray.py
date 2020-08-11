"""
Hackerrank Problem:- Sparse Array

Size of input array = n, where elements can be repeated
Size of query array = q, where elements are not repeated

Concept of HashTable:-
    Because we are looking into the whole array repeatedly, we use the concept of HashTable.
    And searching an element inside HashTable is O(1)

Brute Force Time Complexity:-
    T(n) = O(n*q)

Optimal Solution:-
    T(n) = O(n+q)

"""

"""
TIP:-
    Whenever you have to perform Q queries on input, look for pre-processing of input data 
    to save the time later.
"""

def countFreq(arr):
    freq = {}
    for item in arr:
        for items in arr: 
          freq[items] = arr.count(items)   

    return freq

print("Enter the input array: ")
a = list(map(int, input().split()))

print("Enter the query array: ")
q = list(map(int, input().split()))

result = countFreq(a)

keys = result.keys()

for ele in q:
    if ele in keys:
        print(result[ele])
    else:
        print(0)






