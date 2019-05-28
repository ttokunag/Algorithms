# @param arr: an array-like object to be sorted
def insertion_sort(arr):
    # traverses all elements to see if there are unsorted elements
    for i in range(1, len(arr)):
        target = arr[i]
        insert_idx = i - 1

        while insert_idx >= 0 and target < arr[insert_idx]:
            # moves an element to right by 1 for the element
            # to be inserted
            arr[insert_idx + 1] = arr[insert_idx]
            insert_idx -= 1

        arr[insert_idx + 1] = target
