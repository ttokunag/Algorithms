'''
* Author: Tomoya Tokunaga(mailto: ttokunag@ucsd.edu)
*
* About this file:
* This file implements a binary max-heap structure
'''
class maxheap(object):

    def __init__(self, arr):
        self.arr = arr
        # heapify the given array
        for i in range(int((self.size()/2) - 1), -1, -1):
            self.percolate_down(i, self.size())

    def sort(self):
        # heapify the given array
        for i in range(int((len(self.arr)/2) - 1), -1, -1):
            self.percolate_down(i, self.size())
        # place the max element at the end & heapify the array in the range
        for i in range(len(self.arr)-1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.percolate_down(0, i)

    '''
    * a helper method which places an element at the given index to the 
    * appropriate place in the max heap structure
    * @param idx: the index of the element in the array
    * @param size: the size of the array
    '''
    def percolate_down(self, idx, size):
        # first looks for children nodes
        child_idx = 2*idx + 1
        value = self.arr[idx]

        while child_idx < size:
            max_value = value
            max_idx = -1
            # compares a parent node with its children
            # if a child has a higher priority, swap the parent and the child
            for i in range(2):
                if child_idx + i < size and self.arr[child_idx + i] > max_value:
                    max_value = self.arr[child_idx + i]
                    max_idx = child_idx + i
            # the case a parent has the highest priority
            if max_value == value:
                return
            else:
                self.arr[idx], self.arr[max_idx] = self.arr[max_idx], self.arr[idx]
                idx = max_idx
                child_idx = 2*idx + 1
    
    # a method which pops the root element from the heap
    def heappop(self):
        if self.size() == 0:
            return

        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        popped = self.arr.pop()
        # heapify the array after the pop
        for i in range((self.size()-1) // 2, -1, -1):
            self.percolate_down(i, self.size())

        return popped

    
    # a method returns the number of elements in the heap
    def size(self):
        return len(self.arr)

    # prints the heap in the form of an array
    def to_str(self):
        print(self.arr)
        

        
