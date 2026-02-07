# return [i, j]

# for i in range(nums:
    # complement = target-i
    # if complement in comp_dict:
        # return [i, comp_dict[complement]]
    # else:
        # comp_dict[nums[i]] = i
# return [-1, -1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_dict = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in val_dict:
                return [i, val_dict[complement]]
            else:
                val_dict[num] = i
        return [-1, -1]
