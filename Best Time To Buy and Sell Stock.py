# Best Time to Buy and Sell Stock Problem

# Problem Statement: You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example:
# Given prices = [7,1,5,3,6,4],
# The maximum profit is 5, which can be achieved by buying on day 2 (price = 1) and selling on day 5 (price = 6).

from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
    
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    result = Solution().maxProfit(prices)
    print(result)

# Time Complexity: O(n), where n is the number of elements in the input list. We traverse the list once.
# Space Complexity: O(1), as we are using only a constant amount of extra space.