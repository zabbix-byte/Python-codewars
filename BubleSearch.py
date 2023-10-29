def binary_search(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2
        if array[mid] == x:
            return mid

        elif array[mid] > x:
            return binary_search(array, x, low, mid-1)

        else:
            return binary_search(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binary_search(array, x, 0, len(array)-1)

print(result)
