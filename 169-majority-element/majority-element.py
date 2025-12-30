# O(n) loop once
# hash map maintaining the count of all discovered elements
#   as soon as we update the count of an element we check if count == n/2
#       since majority ele always exists so there wont be 2 elements w n/2 len, so it will be > n/2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = dict()
        half_len = int(len(nums)/2)

        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1

            if counts[i] > half_len:
                return i