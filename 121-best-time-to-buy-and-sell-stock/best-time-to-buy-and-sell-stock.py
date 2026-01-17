# two pointers buy and sell
    # simply buy = lowest seen so far
    # sell = highest seen after buy
# return diff


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        buy = 0
        sell = 0
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            max_diff = max(max_diff, prices[sell]-prices[buy])
            sell+=1
        return max_diff