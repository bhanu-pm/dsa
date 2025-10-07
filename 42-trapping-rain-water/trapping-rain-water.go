func trap(height []int) int {
    if len(height) < 3 {
        return 0
    }
    i := 0
    j := len(height) - 1
    leftmax := 0
    rightmax := 0
    total := 0

    for i < j {
        if height[i] < height[j] {
            if height[i] < leftmax {
                total += leftmax - height[i]
            } else {
                leftmax = height[i]
            }
            i++
        } else {
            if height[j] < rightmax {
                total += rightmax - height[j]
            } else {
                rightmax = height[j]
            }
            j--
        }
    }
    return total
}