"""
Given:- 
An array of non-negative digits that represent a decimal integer.

Problem:-
Add one to the integer. Assume the solution still works even if 
implemented in a language with finite-precision arithmetic.
"""
"""
Additional code
a = [1,4,9]
s = ''.join(map(str, a))
reversed(range(a,b))
"""
#Write your code here
a1 = [1,4,9]
a2 = [9,9,9]

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

print(plus_one(a1))
print(plus_one(a2))