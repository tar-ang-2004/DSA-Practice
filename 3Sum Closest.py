#3Sum Closest Problem

# Problem Statement: Given an array of integers nums and an integer target, return the sum of the three integers in nums such that the sum is closest to target. You may assume that each input would have exactly one solution.

# Example:
# Given nums = [-1, 2, 1, -4], target = 1,
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

from typing import List

class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Initialize with first three elements to avoid repeated abs(inf - target) calls
        closest_sum = nums[0] + nums[1] + nums[2]
        best_diff = abs(closest_sum - target)

        for i in range(n - 2):
            # Optional: skip duplicate `i` values to avoid redundant work
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = current_sum - target
                abs_diff = diff if diff >= 0 else -diff

                if abs_diff < best_diff:
                    best_diff = abs_diff
                    closest_sum = current_sum

                if diff < 0:
                    left += 1
                elif diff > 0:
                    right -= 1
                else:
                    return current_sum

        return closest_sum
    
if __name__ == "__main__":
    import time

    nums = [-1, 2, 1, -4]
    target = 1
    start = time.perf_counter()
    result = Solution().threeSumClosest(nums, target)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(result)
    print(f"Elapsed: {elapsed_ms:.3f} ms")

# Time Complexity: O(n^2), where n is the number of elements in the input list. We have two nested loops.
# Space Complexity: O(1), as we are using only a constant amount of extra space