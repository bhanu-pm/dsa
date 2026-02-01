# values from 3 different indexes
# sum of 3 values = 0, i+j+k=0, j+k=-i
# how do I make sure the sol sets are different?????????????????????????????
# maybe we can maintain a set of all sols
    # and calc all possible sols
# they are not asking for indexes, but only values,
# so sorting is allowed

# sort the input
# for i
    # init j=0, k=len(nums)-1
    # while j<k
        # standard two pointer sol
        # with target sum (j+k) = -i
        # if j or k = i
            # skip, j+= 1 or k -= 1
    # store all possible soln.s in set
# turn set to list and return

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        for i, num in enumerate(nums):
            if i>0 and nums[i-1] == num:
                continue
            target = -nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j] + nums[k] < target:
                    j+=1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:
                    output.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
        return list(output)


#####################################################################################################
# alternate sol.
# use the unsorted 2sum soln, using a hashmap
# output_set
# for i
    # dict()
    # target = -i
    # for j
        # if j in dict
            # 
        # new_target = target-j
        # if new_target in dict:
            # output_set.add([i, j, new_target])
        # else:
            # dict[new_target] = j
    # return list(outputset)

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         output_set = set()
#         seen_i = set()
#         for i in range(len(nums)):
#             if nums[i] not in seen_i:
#                 target = -nums[i]
#                 compl_set = set()

#                 for j in range(i+1, len(nums)):
#                     # j+k=-i, k=-i-j
#                     complement = target-nums[j]
#                     if complement in compl_set:
#                         tup = [nums[i], nums[j], complement]
#                         tup.sort()
#                         output_set.add(tuple(tup))
#                     else:
#                         compl_set.add(nums[j])
#         return list(output_set)