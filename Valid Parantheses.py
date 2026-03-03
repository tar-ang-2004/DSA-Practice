#Valid Parantheses Problem

# Problem Statement: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example:
# Given s = "()",
# The output should be True.

from typing import List

class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
    
if __name__ == "__main__":
    s = "({[]})"
    result = Solution().isValid(s)
    print(result)

# Time Complexity: O(n), where n is the length of the input string. We traverse the string once.
# Space Complexity: O(n), in the worst case, we might store all opening brackets in the stack.