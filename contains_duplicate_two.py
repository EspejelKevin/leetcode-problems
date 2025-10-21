"""

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Explanation: 
    - take the index 0 and index 3: nums[0] = 1 and nums[3] = 1
    - ask if nums[0] and nums[0] are equals, in this case is true: 1 == 1
    - then, calculate abs(i - j): abs(0 - 3) = 3
    - finally, ask if abs(i - j) <= k: 3 <= 3, in this case is true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""

def contains_near_by_duplicate(nums: list[int], k: int) -> bool:
    indices = {}
    for current_index, num in enumerate(nums):
        if (num in indices) and (abs(indices[num] - current_index) <= k):
            return True
        indices[num] = current_index
    return False
