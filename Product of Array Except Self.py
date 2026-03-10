# Product of Array Except Self Problem

# Problem Statement: Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:
# Given nums = [1,2,3,4],
# The output should be [24,12,8,6], because:
# - For index 0: the product of all elements except nums[0] is 2*3*4 = 24
# - For index 1: the product of all elements except nums[1] is 1*3*4 = 12
# - For index 2: the product of all elements except nums[2] is 1*2*4 = 8
# - For index 3: the product of all elements except nums[3] is 1*2*3 = 6

from typing import List

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        # Calculate the product of all elements to the left of each index
        left_product = 1
        for i in range(length):
            output[i] *= left_product
            left_product *= nums[i]

        # Calculate the product of all elements to the right of each index
        right_product = 1
        for i in range(length - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output
    
if __name__ == "__main__":
    nums = [1,2,3,4]
    result = Solution().productExceptSelf(nums)
    print(result)

# Time Complexity: O(n), where n is the number of elements in the input list. We traverse the list twice.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the output array (not counting the output array itself).