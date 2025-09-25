class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, element in enumerate(nums):
            complement = target - element
            if complement in hash:
                return [hash[complement], idx]
            hash[element] = idx
