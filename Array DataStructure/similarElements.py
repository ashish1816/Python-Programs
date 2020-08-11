"""
Given an unsorted list of some elements(may or may not be integers), 
find the frequency of each distinct element in the list using a dictionary.

Input :- [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
Output:- 1 --> 5
         2 --> 4
         3 --> 3
         4 --> 3
         5 --> 2

Concept:-
    Making a dictionary with keys = element and storing the count of element in the value of key.

Time Complexity:-
    T(n) = O(n), where n is the length of the list.
"""

def countFreq(arr):
    freq = {}
    for item in arr:
        #Approach 1
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

        # Approach 2
        # for items in arr: 
        #   freq[items] = arr.count(items)    
    return freq

print("Enter the input array: ")
l = list(map(int, input().split()))

result = countFreq(l)

print("Your hash table for the given input is:- \n", result)