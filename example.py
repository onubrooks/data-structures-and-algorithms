#  Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For Example:
# const array1 = ['a', 'b', 'c', 'x'];# const array2 = ['z', 'y', 'i'];
# should return false.
# -----------
# const array1 = ['a', 'b', 'c', 'x'];# const array2 = ['z', 'y', 'x'];
# should return true.

#  2 parameters - arrays - no size limit
#  return true or false

def contains_common_item_quadratic(arr1, arr2):
  for i in arr1:
    for j in arr2:
        if i == j:
          return True
  return False

# O(a*b)
# O(1) - Space Complexity

def contains_common_item_linear(arr1, arr2):
  # loop through first array and create object where properties === items in the array

  map = {}
  for item in arr1:
    if item not in map:
        map[item] = True
  # loop through second array and check if item in second array exists on created object. 
  for item in arr2:
    if item in map:
        return True
    
  return False

# O(a + b) Time Complexity
# O(a) Space Complexity

def contains_common_item_readable(arr1, arr2):
    return any(item in arr2 for item in arr1)


array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'a']

contains_common_item_quadratic(array1, array2)
contains_common_item_linear(array1, array2)
contains_common_item_linear(array1, array2)