class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = len(nums) * ((len(nums) + 1)/2)
        total = 0
        for i in nums:
            total += i
        return int(expected - total)