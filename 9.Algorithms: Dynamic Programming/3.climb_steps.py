def climb_stairs_bottom_up(n):
    """
    :type n: int
    :rtype: int
    """
    nums = []
    for i in range(n+1):
        if i <= 2:
            nums.append(i)
        else:
            steps = nums[i-1] + nums[i-2]
            nums.append(steps)
    return nums.pop()

print(climb_stairs_bottom_up(8))

def climb_stairs_top_down(n):
    memo = {}
    def climb(steps):
        if steps <= 2:
            return steps
        else:
            # return climb(steps-1) + climb(steps-2)
            if steps in memo:
                return memo[steps]
            else:
                memo[steps] = climb(steps-1) + climb(steps-2)
                return memo[steps]

    return climb(n)

print(climb_stairs_top_down(8))