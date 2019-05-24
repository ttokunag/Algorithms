'''
* Author: Tomoya Tokunaga(mailto: ttokunag@ucsd.edu)
*
'''

def merge_sort(arr):
    # an array length of <= 1 is already sorted
    if len(arr) <= 1:
        return arr
    # set a pivot to divide the given array into two
    pivot = len(arr)//2
    left_arr = merge_sort(arr[:pivot])
    right_arr = merge_sort(arr[pivot:])
    
    '''
    * the following is a helper method to recursively sort subarrayslef
    * @param left_array: the left divided array
    * @param right_array: the right divided array
    '''
    def merge(left_arr, right_arr):
        left_cur = right_cur = 0
        res = []
        # place a smaller element of two arrays to a smaller index
        while left_cur < len(left_arr) and right_cur < len(right_arr):
            if left_arr[left_cur] < right_arr[right_cur]:
                res.append(left_arr[left_cur])
                left_cur += 1
            else:
                res.append(right_arr[right_cur])
                right_cur += 1
        # once one array gets empty, append the other
        res.extend(left_arr[left_cur:])
        res.extend(right_arr[right_cur:])
        return res
    
    return merge(left_arr, right_arr)