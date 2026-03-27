#Minimum Window Substring Problem

# Problem Statement: Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

# Example:
# Given s = "ADOBECODEBANC", t = "ABC",
# The minimum window in s which contains all characters in t is "BANC".

from collections import Counter

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        required = len(t_count)
        formed = 0
        left, right = 0, 0
        window_counts = {}
        min_length = float('inf')
        min_window = ""

        while right < len(s):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in t_count and window_counts[character] == t_count[character]:
                formed += 1

            while left <= right and formed == required:
                character = s[left]

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]

                window_counts[character] -= 1
                if character in t_count and window_counts[character] < t_count[character]:
                    formed -= 1

                left += 1

            right += 1

        return min_window

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    result = Solution().minWindow(s, t)
    print(result)

# Time Complexity: O(m + n), where m and n are the lengths of strings s and t respectively. We traverse s and t a constant number of times.
# Space Complexity: O(m + n), where m and n are the lengths of strings s and t respectively. We use additional space to store character counts.