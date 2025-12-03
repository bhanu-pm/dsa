class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        for i in nums:
            total += i
        return total % k