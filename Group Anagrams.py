#Group Anagrams Problem

# Problem Statement: Given an array of strings, group anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example:
# Given strs = ["eat", "tea", "tan", "ate", "nat", "bat"],
# The output should be [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]. Note that the order of the output does not matter.

from collections import defaultdict
from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            # Sort the string to get the key for the anagram group
            sorted_str = ''.join(sorted(s))
            anagram_dict[sorted_str].append(s)

        return list(anagram_dict.values())
    
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print(result)

# Time Complexity: O(n * k log k), where n is the number of strings in the input list and k is the maximum length of a string. Sorting each string takes O(k log k) time, and we do this for all n strings.
# Space Complexity: O(n * k), in the worst case, all strings are anagrams of each other and we store all n strings in the dictionary, each of length k.