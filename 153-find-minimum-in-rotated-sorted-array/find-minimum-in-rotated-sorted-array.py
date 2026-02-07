# rotating is, last element going to first
# arr has unique elements, ascending inititally
# return minimum

# naive soln
    # just go through and return smallest
    # O(N) time complexity, O(1) space
# we need O(log n) time complexity

# if rotated 0 times or m*len(arr), would result in no change
# else
    # left most element > min(arr)


# if nums[0] > nums[n-1]
    # rotated
    # so find max value
    # i = 0
    # [6, 7, 0, 1, 2, 3, 4, 5]
        # while nums[i]<nums[i+1]:
            # i+=1
        # else:
            # return nums[i+1]
# else nums[0] < nums[n-1]
    # return nums[0]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] > nums[-1]:
            # rotated
            i = 0
            while nums[i]<nums[i+1]:
                i+=1
            else:
                return nums[i+1]
        else:
            # rotated 0 or m*len(nums) times
            return nums[0]