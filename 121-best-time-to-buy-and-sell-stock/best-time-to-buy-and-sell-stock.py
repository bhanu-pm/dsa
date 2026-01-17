# two pointers buy and sell
    # simply buy = lowest seen so far
    # sell = highest seen after buy
# return diff


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        current_min = float('inf')
        current_max = float('-inf')
        buy = 0
        sell = 0
        while sell < len(prices):
            if prices[sell] < current_min:
                current_min = prices[sell]
                buy = sell
                # current_max = float('-inf')
            elif prices[sell] > current_max:
                current_max = prices[sell]
            max_diff = max(max_diff, prices[sell]-prices[buy])
            sell+=1
        return max_diff