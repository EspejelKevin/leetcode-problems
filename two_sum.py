"""

Given an array of integers nums and an integer target,
return indices of the two numbers such thay they add up
to target.

You may assume thay each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0,1]

"""

nums = [2,7,11,15]
target = 9

def two_sum(nums: list, target: int) -> list:
    complements = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return [complements[complement], index]
        complements[num] = index

    return []
