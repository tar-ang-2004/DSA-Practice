#Longest Substrings without Repeating Characters Problem

# Problem Statement: Given a string s, find the length of the longest substring without repeating characters.

# Example:
# Given s = "abcabcbb",
# The longest substring without repeating characters is "abc", which has a length of 3.

from typing import List

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        longest_length = 0
        left = 0

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
            char_index_map[s[right]] = right
            longest_length = max(longest_length, right - left + 1)

        return longest_length
    
if __name__ == "__main__":
    s = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)

# Time Complexity: O(n), where n is the length of the input string. We traverse the string once.
# Space Complexity: O(min(m, n)), where m is the size of the character set and n is the length of the input string. In the worst case, we might store all characters in the current substring in the dictionary.
