# 1. have a base case
# 2. hava a recursive case
# 3. get closer and closer to the base case, and return when needed. Usually you have 2 returns

def find_factorial_recursive(number):
  if number < 3:
    return number
  return number * find_factorial_recursive(number - 1)

def find_factorial_iterative(number):
  if number == 2 or number == 1:
    return number
  answer = 1
  num = 2
  while num <= number:
    answer = answer * num
    num += 1
  return answer

print(find_factorial_recursive(1))
print(find_factorial_recursive(2))
print(find_factorial_recursive(3))
print(find_factorial_recursive(4))

print(find_factorial_iterative(1))
print(find_factorial_iterative(2))
print(find_factorial_iterative(3))
print(find_factorial_iterative(4))