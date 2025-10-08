func longestConsecutive(nums []int) int {
    dict := make(map[int]bool)
    engine := make([]int, 0, len(nums))
    longest := 0
    sequence := 0

    for _, i := range nums {
        dict[i] = true
    }
    
    for key, _ := range dict {
        if _, ok := dict[key-1]; !ok {
            engine = append(engine, key)
        }
    }

    for _, eng := range engine {
        sequence = 1
        for i:=1; i<=len(nums); i++ {
            if _, ok := dict[eng+i]; ok {
                sequence++
            } else {
                break
            }
        }
        if sequence > longest {
            longest = sequence
        }
    }
    return longest
}