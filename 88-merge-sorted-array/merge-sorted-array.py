#  - increasing order with duplicates (both)
#  - final result stored within nums1
#     - so we would need to insert ele from nums2 into nums1, at appropriate location
#     - two pointers
#         - mptr in nums 1, after inserting all the elements of equal value goes to the next one
#         - nptr iterates through its whole list and inserts these nums into nums1 at mptr

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m + n == 0:
            return
        if n == 0:
            return
        
        filler = m+n-1
        mptr = m-1
        nptr = n-1

        while (mptr >= 0) and (nptr >= 0):
            if nums1[mptr] >= nums2[nptr]:
                nums1[filler] = nums1[mptr]
                nums1[mptr] = 0
                mptr -= 1
            else:
                nums1[filler] = nums2[nptr]
                nptr -= 1
            filler -= 1
        
        while nptr >= 0:
            nums1[filler] = nums2[nptr]
            filler -= 1
            nptr -= 1

        return