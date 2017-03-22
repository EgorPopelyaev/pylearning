def shell_sort(arr):

    sub_list_count = len(arr)/2

    while sub_list_count > 0:

        for start in range(sub_list_count):

            gap_insertion_sort(arr, start, sub_list_count)

        print 'After increment of size: ', sub_list_count
        print 'List is: ', arr
        sub_list_count = sub_list_count/2


def gap_insertion_sort(arr, start, gap):

    for i in range(start + gap, len(arr), gap):

        current_value = arr[i]
        position = i

        while position >= gap and arr[position - gap] > current_value:

            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = current_value


arr = [4, 6, 7, 4, 5, 1, 9, 11, 13]
shell_sort(arr)