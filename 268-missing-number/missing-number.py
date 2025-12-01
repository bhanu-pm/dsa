class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # expected = len(nums) * ((len(nums) + 1)/2)
        # total = 0
        # for i in nums:
        #     total += i
        # return int(expected - total)
        seen = set()
        for i in nums:
            seen.add(i)
        for i in range(0, len(nums)+1):
            if i not in seen:
                return i