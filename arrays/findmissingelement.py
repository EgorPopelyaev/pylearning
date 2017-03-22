
def finder(arr1, arr2):
    print list(set(arr1) - set(arr2))

    return list(set(arr1) - set(arr2))

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
finder(arr1,arr2)
