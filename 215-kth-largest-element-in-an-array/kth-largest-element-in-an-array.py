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
        min_heap = []
        heapq.heapify(min_heap)
        for i in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, i)
            else:
                heapq.heappush(min_heap, i)
                heapq.heappop(min_heap)
        return heapq.heappop(min_heap)

        # popped = []
        # heapq.heapify_max(nums)
        # while len(popped) < k-1:
        #     popped.append(heapq.heappop_max(nums))
        # return heapq.heappop_max(nums)
        