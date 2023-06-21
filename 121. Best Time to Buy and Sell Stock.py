class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                curr = prices[right] - prices[left]
                profit = max(profit, curr)
            else:
                left = right
            right += 1

        return profit