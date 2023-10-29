# Bubble sort in Python

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubble_sort(data)

print('Sorted Array in Ascending Order:')
print(data)
