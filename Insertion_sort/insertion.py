# implementation of the Insertion Sort
"""Insertion sort is a simple sorting algorithm that works by dividing an
array into a "sorted" and an "unsorted" region.
It iteratively takes elements from the unsorted region and
inserts them into their correct position in the sorted region."""

# Kind of similar to the bubble SOrt, Insertion does have a better Time Complexity
def insertion_sort(arr):
    j = len(arr)

    """Do a for loop for the ELements inside"""
    for i in range(1, j):
        crr_elem = arr[i] #The unsorted element that needs sorting
        last_index = i - 1 # The Element Before

        while last_index >= 0 and arr[last_index] > crr_elem:
            arr[last_index + 1] = arr[last_index]
            last_index -= 1

        arr[last_index + 1] = crr_elem

    return arr

arry = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
insertion_sort(arry)

print(arry)
