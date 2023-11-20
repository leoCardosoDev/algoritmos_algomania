def factorial(max_number):
  if max_number <= 1:
    return 1
  result = 1
  for each in range(1, max_number + 1):
    result *= each
  return result


print(factorial(5))
