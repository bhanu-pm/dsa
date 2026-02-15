# given unsorted array of ints
# return list of sorted triplets, no duplicate triplets
# sorting should be OK
# max time O(N*logN)

# result = set
# for i
    # unsorted 2 sum of remaining
    # sort the triplet
        # add to result
# return list (result)

######## OR
# sort nums
# for i
    # sorted 2 sum of remaining


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        for i, num in enumerate(nums):
            if i>0 and num==nums[i-1]: # same i
                continue
            complement = set()
            target = -num
            for j in range(i+1, len(nums)):
                compl = target-nums[j]
                if compl in complement:
                    triplet = [num, nums[j], compl]
                    triplet.sort()
                    result.add(tuple(triplet))
                else:
                    complement.add(nums[j])
        
        return list(result)
                