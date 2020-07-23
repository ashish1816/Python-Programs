"""
<!----       *****Array Advance Game*****         -->
You are given an array of non-negative integers.
For example:- [3,3,1,0,2,0,1]
Each number represents the maximum you can advance in the array.

Objective:- 
    Is it possible to advance from the start of the array to the last element?
"""

def array_advance(A):

    furthest_reached = 0
    last_idx = len(A)-1
    i=0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i]+i)
        i += 1
    
    return furthest_reached >= last_idx

A1 = [3,3,1,0,2,0,1]
print(array_advance(A1))

"""
Test Cases:-
A2 = [3,2,0,0,2,0,1]
"""