def merge_sorted_arrays(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    merged_array = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr2[j] > arr1[i]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    return merged_array

print(merge_sorted_arrays([0,3,4,31], [3,4,6,30]))