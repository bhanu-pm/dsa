from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        length = len(nums)

        for idx, element in enumerate(nums):
            if idx > 0 and element == nums[idx - 1]:
                continue

            i, j = idx + 1, length - 1
            while i < j:
                three_sum = element + nums[i] + nums[j]
                if three_sum < 0:
                    i += 1
                elif three_sum > 0:
                    j -= 1
                else:
                    final.append([element, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        
        return final