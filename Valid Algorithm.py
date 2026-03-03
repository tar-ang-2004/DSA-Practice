#Valid Algorithm Problem

# Problem Statement: Given an array of integers, determine if there are any two numbers that add up to a specific target.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return True.

from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> bool:
        # Create a set to store the numbers we have seen
        seen = set()

        # Iterate through the list of numbers
        for num in nums:
            # Calculate the complement of the current number
            complement = target - num

            # Check if the complement is in the set
            if complement in seen:
                # If it is, return True
                return True

            # Otherwise, add the current number to the set
            seen.add(num)

        # If no solution is found, return False
        return False
    
if __name__ == "__main__":
    nums = [1,4,6,8]
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)

# Time Complexity: O(n), where n is the number of elements in the input list. We traverse the list once.
# Space Complexity: O(n), in the worst case, we might store all n elements in the set.