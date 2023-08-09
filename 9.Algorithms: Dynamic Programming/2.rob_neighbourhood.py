"""
Leetcode Challenge: 
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security systems connected and it will 
automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
Example:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""
def rob(nums):
    memo = {}
    def calculate_value(index):
        if index >= len(nums):
            return 0
        else:
            if index in memo:
                return memo[index]
            else:
                memo[index] = max(nums[index] + calculate_value(index+2), calculate_value(index+1))
                return memo[index]
            
    return calculate_value(0)
