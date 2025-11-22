class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: complement -> value: index
        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash:
                return [i, hash[complement]]
            
            # key: current num -> value: i
            hash[nums[i]] = i
        return [-1, -1]