# input int array of heights
# find max area possible from the given heights
# not sortable
# area = min(both heights) * (right-left pointer)

# track a max_area
# while left < right:
    # calc area
    # max_area = max(max_area, area)
    # if heightleft < heightright
        # left++
    # elif >
        # right--
    # else ==
        # left++
        # right--
# return maxarea

# edge case where less than 2 heights given
# return 0


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        
        max_area = float('-inf')
        left = 0
        right = len(height)-1

        while left < right:
            area = min(height[left], height[right]) * (right-left)
            max_area = max(max_area, area)

            if height[left] > height[right]:
                right-=1
            elif height[left] < height[right]:
                left+=1
            else:
                left+=1
                right-=1
        
        return max_area