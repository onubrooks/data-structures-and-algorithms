"""
https://leetcode.com/problems/two-sum/
"""
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        num_to_find = target - nums[i]
        for j in range(i+1, len(nums)):
            if num_to_find == nums[j]:
                return [i, j]
    return None

def two_sum(nums, target):
    nums_to_find = {}
    for i in range(len(nums)):
        curr_val = nums[i]
        if curr_val in nums_to_find:
            return [nums_to_find[curr_val], i]
        else:
            num_to_find = target - curr_val
            nums_to_find[num_to_find] = i
    return None

arr, tar = [3,2,4], 6

print(two_sum_brute_force(arr, tar))
print(two_sum(arr, tar))