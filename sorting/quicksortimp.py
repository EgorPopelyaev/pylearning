def quick_sort(arr):

    quick_sort_helper(arr, 0, len(arr) - 1)
    print 'Sorted array: ', arr


def quick_sort_helper(arr, first, last):

    if first < last:
        split_point = partition(arr, first, last)
        print 'Set a split point: ', split_point

        quick_sort_helper(arr, first, split_point - 1)
        quick_sort_helper(arr, split_point + 1, last)


def partition(arr, first, last):

    pivot_val = arr[first]
    print 'Pivot value: ', pivot_val

    left_mark = first + 1
    print 'Left marker: ', left_mark

    right_mark = last
    print 'Right marker: ', right_mark

    done = False

    while not done:

        while left_mark <= right_mark and arr[left_mark] <= pivot_val:
            print 'Go from left side'
            left_mark += 1

        while arr[right_mark] >= pivot_val and right_mark >= left_mark:
            print 'Go from right side'
            right_mark -= 1

        if right_mark < left_mark:
            print 'Markers crossed'
            done = True
        else:
            print 'Exchange markers values'
            temp = arr[left_mark]
            arr[left_mark] = arr[right_mark]
            arr[right_mark] = temp

    temp = arr[first]
    arr[first] = arr[right_mark]
    arr[right_mark] = temp

    return right_mark

arr = [4, 6, 7, 4, 5, 1, 9, 11, 13]

quick_sort(arr)