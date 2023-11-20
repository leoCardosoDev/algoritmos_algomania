def print_item(my_array):
    for item in my_array:
        print(item)


array1 = [1, 2, 3, 4]
array2 = [9, 7, 6, 5, 4, 3, 2, 1]

print(print_item(array1))
print(print_item(array2))


def find_max(my_array):
    max = 0
    for item in my_array:
        if item > max:
            max = item
    return max


print(find_max(array1))
print(find_max(array2))


def find_sum(my_array):
    sum = 0
    for item in my_array:
        sum += item
    return sum


print(find_sum(array1))
print(find_sum(array2))
