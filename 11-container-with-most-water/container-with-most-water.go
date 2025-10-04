func maxArea(height []int) int {
    i := 0
    j := len(height) - 1
    maxArea := 0
    for i < j {
        area := (j-i) * min(height[i], height[j])
        if area > maxArea {
            maxArea = area
        }
        if height[i] > height[j] {
            j--
        } else if height[i] < height[j] {
            i++
        } else {
            i++
            j--
        }
    }
    return maxArea
}