def find_commom_elements(list1, list2):
  result = []
  for item1 in list1:
    for item2 in list2:
      if item1 == item2:
        result.append(item1)
  return result
array1 = [1, 2, 3, 4]
array2 = [9, 7, 6, 5, 4, 3, 2, 1]

print(array1)
print(array2)
print(find_commom_elements(array1, array2))
