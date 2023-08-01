# Implement a function that reverses a string using iteration...and then recursion!
def reverse_string_iter(str):
  rev = ''
  for i in range(len(str)-1, -1, -1):
    rev += str[i]
  return rev


def reverse_string_recur(str):
  if len(str) < 2:
    return str
  return reverse_string_recur(str[1:]) + str[0]

print(reverse_string_iter('yoyo mastery'))
print(reverse_string_recur('yoyo mastery'))
# should return: 'yretsam oyoy'