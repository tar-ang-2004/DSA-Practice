# 2Sum problem

# Problem Statement: Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of the numbers
        num_dict = {}

        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in num_dict:
                # If it is, return the indices of the two numbers
                return [num_dict[complement], i]

            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i

        # If no solution is found, return an empty list (though the problem guarantees one solution)
        return []

if __name__ == "__main__":
    nums = [2,4,6,8]
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)

# Time Complexity: O(n), where n is the number of elements in the input list. We traverse the list once.
# Space Complexity: O(n), in the worst case, we might store all n elements in the dictionary.



