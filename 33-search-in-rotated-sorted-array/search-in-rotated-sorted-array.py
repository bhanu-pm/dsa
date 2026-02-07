# 1 rotation is last element popped and inserted in first
# unique values, ascending initially
# k = [1, len)
# if target in nums
    # return index
# else
    # return -1


# if rotated: do all the below
# if nums[0] == target:
    # return 0
# elif target > nums[0]:
    # anything bigger than nums[0] would be in rotated part
    # i = 1
    # [4, 5, 6, 8, 0, 1, 2], target 7
    # while target > nums[i] and nums[i] > nums[0]
        # i+=1
    # else
        # if target == nums[i]
            # return i
        # else: ???????????????????????????????? should work
            # return -1
# elif target < nums[0]:
    # anything < nums[0] would be in unrotated part
    # i = len(nums)-1
    # while target < nums[i] and nums[i] < nums[-1]:
        # i-=1
    # else:
        # if target == nums[i]
            # return i
        # else:
            # return -1
# if unrotated (nums[0] < nums[-1])
    # do binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > nums[-1]:
            # rotated
            if nums[0] == target:
                return 0
            elif target > nums[0]:
                # within the rotated part
                i = 1
                while target > nums[i] and nums[i] > nums[0]:
                    i+=1
                else:
                    if target == nums[i]:
                        return i
                    else:
                        return -1
            elif target < nums[0]:
                # within the unrotated part
                i = len(nums)-1
                while target < nums[i] and nums[i] < nums[0]:
                    i-=1
                else:
                    if target == nums[i]:
                        return i
                    else:
                        return -1
        else:
            # unrotated
            return self.bsearch(nums, target)
    
    def bsearch(self, nums, target):
        left = 0
        right = len(nums)-1

        while True:
            idx = (left+right)//2
            if target == nums[idx]:
                return idx
            if left == right:
                return -1
            elif target > nums[idx]:
                left = idx+1
            elif target < nums[idx]:
                right = idx