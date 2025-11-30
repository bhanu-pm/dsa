class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        slow = 1

        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow
