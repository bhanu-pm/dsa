class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        length = len(nums)

        for idx, element in enumerate(nums):
            i = idx + 1
            j = length - 1

            if (idx > 0) and (element == nums[idx-1]):
                continue
            target = -element

            while i < j:
                if (i > idx + 1) and (nums[i] == nums[i-1]):
                    i += 1
                    continue
                
                if (j < len(nums) - 1) and (nums[j] == nums[j+1]):
                    j -= 1
                    continue
                
                summ = nums[i] + nums[j]

                if summ == target:
                    output.append([element, nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif summ < target:
                    i += 1
                else:
                    j -= 1
            
        return output