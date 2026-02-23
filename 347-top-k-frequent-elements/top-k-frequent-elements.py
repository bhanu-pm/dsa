# given nums arr, k
# return k most frequent elements

# heap should be faster than sorting
# top k most frequent
    # so max heap, ordered by max frequency

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        for i in nums:
            if i not in frequencies:
                frequencies[i] = 0
            frequencies[i] += 1
        topk = []
        for i in list(frequencies.keys()):
            topk.append((frequencies[i], i))
        
        final = []
        heapq.heapify_max(topk)
        for i in range(k):
            top = heapq.heappop_max(topk)
            final.append(top[1])
        return final