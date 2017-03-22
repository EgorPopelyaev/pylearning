def insertion_sort(arr):

    for i in range(1, len(arr)):

        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:

            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value

    print arr

arr = [4, 6, 7, 4, 5, 1, 9, 11, 13]

insertion_sort(arr)
