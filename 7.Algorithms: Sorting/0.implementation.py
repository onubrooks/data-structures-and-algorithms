numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubble_sort(array):
    length = len(array)
    for _ in range(length):
        for i in range(length):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp

# bubble_sort(numbers)
# print(numbers)

def selection_sort(numbers):
    for i in range(len(numbers)):
        min = i
        temp = numbers[i]
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min]:
                min = j
        numbers[i] = numbers[min]
        numbers[min] = temp
    return numbers

selection_sort(numbers)
print(numbers)

def insertion_sort(numbers):
    pass

insertion_sort(numbers)
print(numbers)