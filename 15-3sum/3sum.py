# given unsorted array of ints
# return list of sorted triplets, no duplicate triplets
# sorting allowed
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
        nums.sort()
        l = len(nums)

        for i, num in enumerate(nums):
            if i>0 and num==nums[i-1]:
                continue
            target = -num
            j = i+1
            k = l-1
            while j<k:
                summ = nums[j] + nums[k]
                if summ == target:
                    result.add(tuple([num, nums[j], nums[k]]))
                    j+=1
                    k-=1
                elif summ < target:
                    j+=1
                elif summ > target:
                    k-=1
        return list(result)