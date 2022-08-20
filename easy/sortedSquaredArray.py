def sortedSquaredArray(array):
    squared_array = []
    if array[0] >= 0:
        first_positive_index = 0
    else:
        first_positive_index = get_first_positive_index(array)
    right_pointer = first_positive_index
    left_pointer = first_positive_index - 1
    while len(squared_array) < len(array):
        if left_pointer < 0 or right_pointer < len(array) and abs(array[left_pointer]) >= abs(array[right_pointer]):
            squared_array.append(array[right_pointer] ** 2)
            if right_pointer > 0:
                right_pointer += 1
            else:
                right_pointer -= 1
        else:
            squared_array.append(array[left_pointer] ** 2)
            left_pointer -= 1
    return squared_array


def get_first_positive_index(array):
    for index, elem in enumerate(array):
        if elem > 0:
            return index
    return -1


if __name__ == '__main__':
    print(sortedSquaredArray([1, 2, 3]))
    print(sortedSquaredArray([-3, -2, -1]))
    print(sortedSquaredArray([0, 0, 0]))
    print(sortedSquaredArray([-6, 1, 2, 3]))
    print(sortedSquaredArray([-5, -3, 2, 4]))
    print(sortedSquaredArray([-5, -3, 2, 4, 6]))
    print(sortedSquaredArray([-7, -5, -3, 4, 6]))
    print(sortedSquaredArray([-11, -2, -1, 0]))