def find_sum(my_array):
  sum = 0
  for item in my_array:
    sum += item
  return sum


array1 = [1, 2, 3, 4]
array2 = [9, 7, 6, 5, 4, 3, 2, 1]

print(find_sum(array1))
print(find_sum(array2))
