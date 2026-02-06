# n piles, ith pile has piles[i] bananas
# h hours time limit
# speed = k bananas/hour
# return minimum k

# she has to eat ALL the bananas
# if pile has < k bananas
    # she eats those bananas and rest
# if pile has > k bananas
    # she eats k and leaves rest for next turn

# if len(piles) == h
    # return max(piles)

# brute force
# try all values of k from min(piles), to max(piles)
    # O(N**2)
# try binary search on min(piles), to max(piles)
    # if valid:
        # select left subarra
    # else
        # select right subarr

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        piles.sort()
        left = 1
        right = piles[-1]
        last_valid = right

        while True:
            val = (left+right)//2
            validity = self.valid(piles, h, val)
            if validity:
                last_valid = min(last_valid, val)
                if left >= right:
                    break
                right = val
            elif not validity:
                if left >= right:
                    break
                left = val+1
        return last_valid
        
    def valid(self, piles, h, k):
        steps = 0
        for i in piles:
            steps += math.ceil(i/k)
        if steps <= h:
            return True
        return False