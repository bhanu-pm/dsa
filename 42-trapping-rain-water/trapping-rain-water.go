func trap(height []int) int {
    if len(height) < 3 {
        return 0
    }

    left_max := 0
    right_max := 0
    left := 0
    right := len(height) - 1
    total := 0

    for left <= right {
        lh := height[left]
        rh := height[right]

        if lh < rh {
            if left_max > lh {
                total += left_max - lh
            } else {
                left_max = lh
            }
            left++
        } else {
            if right_max > rh {
                total += right_max - rh
            } else {
                right_max = rh
            }
            right--
        }
    }
    return total
}