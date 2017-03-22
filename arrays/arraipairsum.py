

def pair_sum(arr, k):

    if len(arr) < 2:
        print "Array should contain at least 2 elements"
        return

    count = 0
    pairs_found = 0

    while count < len(arr) - 1:

        current_pair_sum = arr[count] + arr[count + 1]

        if current_pair_sum == k:
            pairs_found += 1
            print "Pair found %d, %d" % (arr[count], arr[count + 1])

        count += 1

    return pairs_found

pair_sum([11,3,23,2,3,12],4)