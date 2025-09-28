class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            i_height = height[i]
            j_height = height[j]
            area = (j-i) * min([i_height, j_height])
            if area > max_area:
                max_area = area
            
            if i_height < j_height:
                i += 1
            elif i_height > j_height:
                j -= 1
            else:
                i += 1
        
        return max_area