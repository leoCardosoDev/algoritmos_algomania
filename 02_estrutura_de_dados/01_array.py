my_array = [1,2,3, 'teste', False, True, 0.1]
print(my_array[0])
print(my_array[-1])
print(my_array[1:3])

num = [23,56,7,8,34,5,6,71,2,22,88]
num.sort()
print(num)
from bisect import bisect
n = bisect(num, 5)
print(n)

