# implementation of the Insertion Sort
"""Insertion sort is a simple sorting algorithm that works by dividing an
array into a "sorted" and an "unsorted" region.
It iteratively takes elements from the unsorted region and
inserts them into their correct position in the sorted region."""

def insertion_sort(arr):
    n = len(arr)

    """Outer loop loops through the List"""
    for i in range(1, n):
        element = arr[i] #Stands for the element that will iteratively be sorted
        last_element = i -1 #element before the current element

        while last_element >= 0 and arr[last_element] > element:
            arr[last_element + 1] = arr[last_element]
            last_element -= 1

    return arr


array = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]

insertion_sort(array)

print(array)


