# i, j, k shouldn't be equal
# sum = 0, so, numj+numk = -numi
# 10**5, so should be less than O(n**2)
# input array, output list(list(int))
# we don't need the exact indices, but only the values, so SORTING ALLOWED

# there might be duplicates, so we sort the triplets themselves and store in an output set.
# sort input arr
# for i
    # skip i values that are same
    # while j<k:
        # if < target
            # j++
        # elif > target
            # k--
        # else
            # output.add(sort(triplet))
# return List(output)

# time complex < O(N**2)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        l = len(nums)-1

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx-1]:
                continue
            left=idx+1
            right = l
            target = -num
            while left < right:
                if nums[left] + nums[right] < target:
                    left+=1
                elif nums[left] + nums[right] > target:
                    right-=1
                else:
                    triplet = [num, nums[left], nums[right]]
                    triplet.sort()
                    output.add(tuple(triplet))
                    left+=1
                    right-=1
        
        return list(output)