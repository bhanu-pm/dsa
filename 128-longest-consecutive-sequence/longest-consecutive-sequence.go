func longestConsecutive(nums []int) int {
    dict := make(map[int]bool)

    for _, i := range nums {
        dict[i] = true
    }

    longest := 0
    engine := make([]int, 0, len(nums))
    for key, _ := range dict {
        if _, ok := dict[key-1]; !ok {
            engine = append(engine, key)
        }
    }

    for _, eng := range engine {
        sequence := 1
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