from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            price_diff = prices[right] - prices[left]
            if price_diff < 0:
                left = right
            if price_diff > max_profit:
                max_profit = price_diff
            right += 1
        return max_profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    out = Solution().maxProfit(prices)
    print(out)
