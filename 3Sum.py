#3Sum Problem

# Problem Statement: Given an array of integers, find all unique triplets in the array which gives the sum of zero. You may assume that the input array is not sorted.

# Example:
# Given nums = [-1, 0, 1, 2, -1, -4],
# A solution set is: [[-1, 0, 1], [-1, -1, 2]].

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to make it easier to avoid duplicates
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate values for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
    
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    result = Solution().threeSum(nums)
    print(result)
    
# Time Complexity: O(n^2)
# Space Complexity: O(k), where k is the number of triplets found.