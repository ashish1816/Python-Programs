#Calculating the first, second and third quartile of a given array

def median(arr, start, end):
    #if array length is even
    if((end+start)%2==0):
        mid = (end+start)//2
        a1 = arr[mid]
        a2 = arr[mid-1]
        centre = (a1+a2)/2
        left_arr_end = mid
        right_arr_start = mid
        return (centre, left_arr_end, right_arr_start)
    #if array length is odd
    else:
        mid = (end+start)//2
        centre = arr[mid]
        left_arr_end = mid
        right_arr_start = mid+1
        return (centre, left_arr_end, right_arr_start)

arr=[1,2,3,4,5,6,7,8]
arr.sort()
l = len(arr)
(q2, l2, r2) = median(arr, 0, l)
(q1, l1, r1) = median(arr, 0, l2)
(q3, l3, r3) = median(arr, r2, l)

print("The first quartile is", q1)
print("The second quartile is", q2)
print("The third quartile is", q3)
