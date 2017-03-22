arr = [4, 6, 7, 4, 5, 1, 9, 11, 13]


def bubble_sort(arr):

    for el in range(len(arr) - 1, 0, -1):

        for start in range(el):

            if arr[start] >= arr[el - 1]:
                temp = arr[start]
                arr[start] = arr[el - 1]
                arr[el - 1] = temp

    print 'Bubble sort: ', arr

#bubble_sort(arr)


def selection_sort(arr):

    for fill_slot in range(len(arr) - 1, 0, -1):

        max_pos = 0

        for current_pos in range(1, fill_slot + 1):
            if arr[current_pos] > arr[max_pos]:
                max_pos = current_pos

        temp = arr[fill_slot]
        arr[fill_slot] = arr[max_pos]
        arr[max_pos] = temp

    print 'Selection sort: ', arr

selection_sort(arr)


def insertion_sort(arr):

    for el in range(len(arr) -1, 0 -1):

        position = 0

        if position > 0 and arr[position] > arr[el]:

            arr[position] = arr[position - 1]
            position -= 1

        arr[position - 1] = arr[el]

    print 'Insertion sort: ', arr

insertion_sort(arr)