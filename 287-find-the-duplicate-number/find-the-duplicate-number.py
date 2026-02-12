# array containing n+1 integers, each integer is from range [1, n] inclusive
# only 1 interger in the array is duplicate, 2 or more times
# use constant extra space to solve it
# can't modify nums, so no sorting
# return the duplicate number

# brute force O(n**2)
    # we can select 1 element and compare all other elements with it

# if we consider indices as box numbers and value in indices as pointers to next box
# a little similar to that veritasium video about prisoners pulling out their number from boxes

# if indices = values
    # the values in index = pointer to next value
    


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow2