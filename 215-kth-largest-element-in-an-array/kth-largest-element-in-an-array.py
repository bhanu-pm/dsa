# given array, k
# return the kth largest element

# make it a max heap
# while popped len < k
    # popped.append(heappop())
# return popped.pop()

###################################
# alternative approach
# kth largest, so in a min heap of size k, it would be the top



import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        popped = []
        last = 0
        heapq.heapify_max(nums)
        while last < k-1:
            popped.append(heapq.heappop_max(nums))
            last += 1
        return heapq.heappop_max(nums)
        