def bubble_sorts(arr):

    for n in range(len(arr) - 1, 0, -1):
        print "N: ", n
        for k in range(n):
            print "K: ", k
            print arr[k],"+",arr[k+1]
            if arr[k] > arr[k + 1]:
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp
    print arr


arr = [5, 3, 7, 2]

bubble_sorts(arr)