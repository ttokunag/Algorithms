'''
* Author: Tomoya Tokunaga(mailto: ttokunag@ucsd.edu)
'''
class maxheap(object):
    def sort(arr):
        '''
        * a helper method which places an element at the given index to the 
        * appropriate place in the max heap structure
        * @param arr: an array which the element is in
        * @param idx: the index of the element in the array
        * @param size: the size of the array
        '''
        def percolate_down(arr, idx, size):
            # first looks for children nodes
            child_idx = 2*idx + 1
            value = arr[idx]

            while child_idx < size:
                max_value = value
                max_idx = -1
                # compares a parent node with its children
                # if a child has a higher priority, swap the parent and the child
                for i in range(2):
                    if child_idx + i < size and arr[child_idx + i] > max_value:
                        max_value = arr[child_idx + i]
                        max_idx = child_idx + i
                # the case a parent has the highest priority
                if max_value == value:
                    return
                else:
                    arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
                    idx = max_idx
                    child_idx = 2*idx + 1

        # heapify the given array
        for i in range(int((len(arr)/2) - 1), -1, -1):
            percolate_down(arr, i, len(arr))
        # place the max element at the end & heapify the array in the range
        for i in range(len(arr)-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            percolate_down(arr, 0, i)
        
        
        
        
