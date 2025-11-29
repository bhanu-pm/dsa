class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}
        # key remaining, val index
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in compl:
                return [i, compl[remaining]]
            compl[nums[i]] = i
        
        return [-1, -1]