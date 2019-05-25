'''
* Author: Tomoya Tokunaga(mailto: ttokunag@ucsd.edu)
'''

class quick_sort(object):
    # O(nlogn) time | O(logn) space
    def sort(arr):
        # helper method is defined below
        helper(arr, 0, len(arr)-1)
        
        '''
        * a helper method to "parition"(sort) an array into two,
        * that is, lower than a pivot & larger than a pivot.
        * @param arr: an array to be partitioned
        * @param low_idx: a lower bound of the partition range
        * @param high_idx: a higher bound of the partition range
        '''
        def partition(arr, low_idx, high_idx):
            # sets a pivot the higher index this time
            pivot = high_idx
            i = low_idx
            for j in range(low_idx, high_idx):
                if arr[j] < arr[pivot]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[high_idx] = arr[high_idx], arr[i]
            # returns a center index of the partitioned array
            return i
        '''
        * another helper method which actually call the above partition
        * method recursively
        '''
        def helper(arr, low_idx, high_idx):
            if low_idx < high_idx:
                p = partition(arr, low_idx, high_idx)
                helper(arr, low_idx, p-1)
                helper(arr, p+1, high_idx)

        
