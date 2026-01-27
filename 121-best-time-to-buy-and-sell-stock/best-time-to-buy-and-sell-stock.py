# given arr
# dynamic subwindow
# don't care about index in the output

# track max_diff = 0 , since we return 0 if no soln.
# track min_val
# buy = 0
# for sell in range()
    # if val < min_val
        # min_val = val
        # this is the new buy val
    # max_diff = max(max_diff, diff)
# return maxdiff


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        min_val = float('inf')
        buy = 0

        for sell in range(len(prices)):
            if prices[sell] < min_val:
                min_val = prices[sell]
                buy = sell
            max_diff = max(max_diff, prices[sell]-prices[buy])
        
        return max_diff