func containsDuplicate(nums []int) bool {
    seen := make(map[int]int, len(nums))

    for _, num := range nums{
        if _, exists := seen[num]; exists{
            return true
        }
        seen[num] = 1
    }
    return false
}