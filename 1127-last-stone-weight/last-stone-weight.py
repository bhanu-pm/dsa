# given weights of stones
# each turn
    # pick heaviest two stones, x and y
    # x <= y
    # if x == y:
        # both destroyed
    # if x < y:
        # x destroyed
        # y = y-x, new weight of y
# maximum only one stone left at end

# make it a max heap
# loop
    # pop y, pop x
    # if y-x > 0
        # push result to max heap


import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            result = y-x
            if result > 0:
                heapq.heappush_max(stones, result)
        else:
            if len(stones) == 1:
                return stones[0]
        return 0
        