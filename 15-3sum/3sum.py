class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        length = len(nums)

        for idx, element in enumerate(nums):
            if (idx > 0) and (element == nums[idx-1]):
                continue

            i = idx + 1
            j = length - 1

            while i < j:
                summ = element + nums[i] + nums[j]

                if (i > idx + 1) and (nums[i] == nums[i-1]):
                    i += 1
                    continue
                
                if (j < length - 1) and (nums[j] == nums[j+1]):
                    j -= 1
                    continue

                if summ == 0:
                    output.append([element, nums[i], nums[j]])
                    i += 1
                    j -= 1

                    while (i < j) and (nums[i] == nums[i-1]):
                        i += 1
                    while (i < j) and (nums[j] == nums[j+1]):
                        j -= 1
                elif summ < 0:
                    i += 1
                else:
                    j -= 1
            
        return output