class binary_search(object): 
    '''
    * a method to find the given target in the given array. if the
    * target is found, then return the index of it. Otherwise None
    * @param arr: an array to be searched
    * @param target: an element the program looks for
    '''
    def find(arr, target):
        # set min and max index to find a median
        left, right = 0, len(arr)-1
        # search an array interatively
        while left <= right:
            med = (left + right)//2
            # the case it finds the exact position
            if target == arr[med]:
                return med
            # if the target is smaller, explore the left half
            elif target < arr[med]:
                right = med - 1
            # if the target is larger, explore the right half
            else:
                left = med + 1

        # if the target is not found, return None
        return None

    # O(log(N)) time | O(1) space
