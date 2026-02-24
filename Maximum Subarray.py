# Maximum Subarray Problem

# Problem Statement: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:
# Given nums = [-2,1,-3,4,-1,2,1,-5,4],
# The contiguous subarray [4,-1,2,1] has the largest sum = 6.

from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0

        return max_sum
    
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = Solution().maxSubArray(nums)
    print(result)

# Time Complexity: O(n), where n is the number of elements in the input list. We traverse the list once.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
