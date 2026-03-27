#Merge Intervals Problem

# Problem Statement: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example:
# Given intervals = [[1,3],[2,6],[8,10],[15,18]],
# The output should be [[1,6],[8,10],[15,18]], because:
# - Intervals [1,3] and [2,6] overlap and are merged into [1,6].

from typing import List

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last_merged = merged[-1]

            # Check if the current interval overlaps with the last merged interval
            if current[0] <= last_merged[1]:  # Overlap condition
                # Merge the intervals by updating the end time
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add the current interval to the merged list
                merged.append(current)

        return merged
    
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = Solution().merge(intervals)
    print(result)

# Time Complexity: O(n log n), where n is the number of intervals. Sorting the intervals takes O(n log n) time, and merging takes O(n) time.
# Space Complexity: O(n), in the worst case, all intervals are non-overlapping and we need to store all of them in the merged list.
