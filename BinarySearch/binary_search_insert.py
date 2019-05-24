def bin_search_insert(arr, target):
    
    # set min & max index in order to find median index
    left, right = 0, len(arr)-1
    
    # iteratively search where the target fits in
    while left != right:
        med = (left + right)//2
        # the case it finds the exact position
        if target == arr[med]:
            arr.insert(med, target)
            return
        # if target less than the median, explore the left half
        elif target < arr[med]:
            # the case the target is larger than the value right before the median
            if not med-1 < 0 and target >= arr[med-1]:
                arr.insert(med, target)
                return
            right = med - 1
        # if target is larger than the median
        else:
            if not med+1 > len(arr)-1 and target <= arr[med+1]:
                arr.insert(med+1, target)
                return
            left = med + 1
            
    # if the right/left cursor reaches the either ends
    if left == len(arr)-1:
        arr.append(target)
    else:
        arr.insert(0,target)

    # O(log(n) + n) time | O(1) space
