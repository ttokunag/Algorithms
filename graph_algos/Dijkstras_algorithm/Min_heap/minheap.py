'''
* Author: Tomoya Tokunaga(mailto: ttokunag@ucsd.edu)
*
* About this file:
* This file implements a binary Min-Heap especially for Dijkstra's
* algorithm. This class assumes that a graph_node class in dijkstra.py
* You can find the attributes of the class at the bottom of this file
'''

class Minheap(object):
    # @param arr: a list of graph nodes
    def __init__(self, arr):
        self.arr = arr
        # heapify the given array
        for i in range((len(arr)-1)//2, -1, -1):
            self.percolate_down(i, len(arr))

    '''
    * a method to place a node at the proper position in the heap
    * @param idx: the index of the element to be heapified
    * @param size: the size of the array the element is in
    '''
    def percolate_down(self, idx, size):
        # first looks for children nodes
        child_idx = 2*idx + 1
        value = self.arr[idx].distance

        while child_idx < size:
            min_value = value
            min_idx = -1
            # compares a parent node with its children
            # if a child has a higher priority, swap the parent and the child
            for i in range(2):
                if child_idx + i < size and self.arr[child_idx + i].distance < min_value:
                    min_value = self.arr[child_idx + i].distance
                    min_idx = child_idx + i
            # the case a parent has the highest priority
            if min_value == value:
                return
            else:
                self.arr[idx], self.arr[min_idx] = self.arr[min_idx], self.arr[idx]
                idx = min_idx
                child_idx = 2*idx + 1
    
    # a method to pop the root of the heap, that is,
    # the minimun element in the heap
    def heappop(self):
        # return nothing if the heap is empty
        if len(self.arr) == 0:
            return
        # pops the minimum element
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        popped = self.arr.pop()
        # heapify the array after the pop
        for i in range((len(self.arr)-1) // 2, -1, -1):
            self.percolate_down(i, len(self.arr))

        return popped
    
    # a method returns the number of elements in the heap
    def size(self):
        return len(self.arr)
    
    def peek(self):
        if len(self.arr) == 0:
            return
        return self.arr[0]

    # a method which prints the elements of the heap in the array form
    def to_str(self):
        res = [node.val for node in self.arr]
        print(res)



        