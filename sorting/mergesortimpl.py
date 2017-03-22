def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr)/2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            print 'Enter first while'
            if left_half[i] < right_half[j]:
                print 'write left'
                arr[k] = left_half[i]
                i += 1
            else:
                print 'write right'
                arr[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            print 'Enter second while and write left'
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            print 'Enter third while and write right'
            arr[k] = right_half[j]
            j += 1
            k += 1
    print 'Merging: ', arr

arr = [4, 6, 7, 4, 5, 1, 9, 11, 13]
merge_sort(arr)