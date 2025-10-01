class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 9999
        output = 0
        for today in prices:
            diff = today - mini

            if diff > output:
                output = diff

            if mini > today:
                mini = today
        
        return output