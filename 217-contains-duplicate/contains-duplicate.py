# int arr given
# if duplicate
    # return True
# else
    # return False

# hash map seen
# for i
    # if i in seen
        # return True
    # seen.add (i)
# return False



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False