# first we check between the first two elements to find inc or dec
# then we do the verification loop

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        i = 0
        j = 1

        if nums[i] > nums[j]:
            # decreasing
            return self.decreasing(nums)
        elif nums[i] < nums[j]:
            # increasing
            return self.increasing(nums)
        else:
            while j < len(nums) and nums[i] == nums[j]:
                i+=1
                j+=1
            else:
                if j == len(nums):
                    return True
                elif nums[i] > nums[j]:
                    return self.decreasing(nums)
                elif nums[i] < nums[j]:
                    return self.increasing(nums)
    
    def decreasing(self, nums):
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] < nums[j]:
                return False
            i+=1
            j+=1
        return True
    
    def increasing(self, nums):
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] > nums[j]:
                return False
            i+=1
            j+=1
        return True