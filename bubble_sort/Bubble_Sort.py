# Implementation of a bubble sort
# Write a function that sorts an array of integers in ascending order using the Bubble sort algorithm
#
# You’re expected to print the array after each time you swap two element

def bubble_sort(array_to_be_sorted):
    """Get The Length Of the Array"""
    n = len(array_to_be_sorted)

    """Loop Through The Elements in the Array"""
    for i in range(n- 1):
        swapped = False

        """Get The next Element since The last indexed to be looped has been sorted"""
        for j in range(n - i - 1):
            if array_to_be_sorted[j] > array_to_be_sorted[j + 1]:
                array_to_be_sorted[j], array_to_be_sorted[j + 1] = array_to_be_sorted[j + 1], array_to_be_sorted[j]
                swapped =  True

        if not swapped:
            break


arr = [19, 48, 71, 99, 13, 52, 96, 73, 86, 7]

bubble_sort(arr)

print(arr)
