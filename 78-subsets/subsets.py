# maybe we can have a tracker
# if 0 don't select the element
# if 1 select the element


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                subsets.append(subset.copy())
                return
            # include
            subset.append(nums[i])
            dfs(i+1)
            # include
            subset.pop()
            dfs(i+1)
        dfs(0)
        return subsets