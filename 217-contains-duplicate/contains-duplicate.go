func containsDuplicate(nums []int) bool {
    seen := make(map[int]int)

    for _, num := range nums{
        _, exists := seen[num]
        if exists{
            return true
        }
        seen[num] = 1
    }
    return false
}