# input sorted array, ascending order
# if target
    # return idx
# else
    # return -1

# O(logN)
# left, right to maintain and denote the sub arrays
# while loop
    # calc idx
        # idx = left+right//2
    # if target = num[idx]
        # return idx
    
    # if left == right
        # return -1
    
    # if target < 
        # right = idx
    # elif target > 
        # left = idx+1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while True:
            idx = (left+right)//2
            if target == nums[idx]:
                return idx
            if left == right:
                return -1
            if target < nums[idx]:
                right = idx
            elif target > nums[idx]:
                left = idx + 1