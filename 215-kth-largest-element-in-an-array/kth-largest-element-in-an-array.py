# given array, k
# return the kth largest element

# make it a max heap
# while popped len < k
    # popped.append(heappop())
# return popped.pop()


import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        popped = []
        heapq.heapify_max(nums)
        while len(popped) < k:
            popped.append(heapq.heappop_max(nums))
        return popped[-1]