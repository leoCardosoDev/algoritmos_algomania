def fibbonacci1(num):
  if num <= 1:
    return num
  return fibbonacci1(num -2) + fibbonacci1(num -1)

n = fibbonacci1(5)
print(n)

memo = {}
def fibbonacci(num):
  if num <= 1:
    return num
  if num not in memo: 
    memo[num] = fibbonacci(num - 1) + fibbonacci(num - 2)
  return memo[num]

print(fibbonacci(5))
print(fibbonacci(10))
