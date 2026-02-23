# for kth largest, we can use the min heap of size k
    # this will have the k biggest values
    # so top of this min heap will have kth biggest val
# since we add elements and not remove
    # just tracking k biggest in a min heap is good



import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.heapif()

    def heapif(self):
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)