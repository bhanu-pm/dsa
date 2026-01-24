# two pointers, dynamic
# track max price diff
# track least price val
# loop
    # check if the current pointer val is less than least price
        # if yes, this is the new buy
        # update least price
    # calc, price diff and update the max price diff accordingly
# return max diff

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        least_price = float('inf')
        max_diff = float('-inf')

        for sell in range(len(prices)):
            if prices[sell] < least_price:
                least_price = prices[sell]
                buy = sell
            max_diff = max(max_diff, prices[sell]-prices[buy])
        
        return max_diff