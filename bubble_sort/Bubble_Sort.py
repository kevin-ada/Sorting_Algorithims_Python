# Implementation of a bubble sort

def bubble_sort(arr):
    arr_len = len(arr)

    for i in range(arr_len - 1):

        swapped = True

        if not swapped:
            break


        for j in range(arr_len - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True


arr = [1,2,3,4,5,5,6,7,8,9,0,0,20,30,40,50,60]

bubble_sort(arr)

print(arr)