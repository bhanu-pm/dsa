func topKFrequent(nums []int, k int) []int {
    if len(nums) < 2 {
        return nums
    }

    counts := make(map[int]int)
    reverse_counts := make(map[int][]int)
    result := []int{}
    for _, num := range nums {
        counts[num]++
    }

    for num, count := range counts {
        reverse_counts[count] = append(reverse_counts[count], num)
    }

    i := len(nums)
    j := 0
    for len(result) < k {
        if list, ok := reverse_counts[i]; ok {
            if j < len(list) {
                result = append(result, list[j])
                j++
            } else {
                j=0
                i--
            }
        } else {
            i--
        }
    }
    return result
}