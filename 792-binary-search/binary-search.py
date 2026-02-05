# sorted in ascending order, input
# find target int
# if target:
    # return idx
# else
    # return -1


# we can use left and right pointers to indicate a sub arr/ range
# left inclusive, right exclusive [left, right)
# while sub list exist: (condition right-left>0)
    # current idx = int(right+left/2)
    # if i == target
        # return idx
    # elif target < i
        # new sub list, to left,
            # right = current idx, no need to change left
    # else
        # new sub list, to right
            # left = current idx + 1, don't change right
# return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while True:
            idx = int((right+left)/2)
            if nums[idx] == target:
                return idx
            if right == left:
                break
            if target < nums[idx]:
                right = idx
            elif target > nums[idx]:
                left = idx+1
        return -1