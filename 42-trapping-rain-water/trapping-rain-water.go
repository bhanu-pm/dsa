func trap(height []int) int {
    if len(height) < 3 {
        return 0
    }

    total := 0
    i := 0
    j := len(height) - 1
    leftmax := 0
    rightmax := 0

    for i<j {
        if height[i] > height[j] {
            if height[j] >= rightmax {
                rightmax = height[j]
            } else {
                total += rightmax - height[j]
            }
            j--
        } else {
            if height[i] >= leftmax {
                leftmax = height[i]
            } else {
                total += leftmax - height[i]
            }
            i++
        }
    }
    return total
}