func characterReplacement(s string, k int) int {
    longest := 0
    left := 0
    maxJ := 0
    counts := make(map[byte]int)

    for right, letter := range s {
        counts[byte(letter)]++
        for _, j := range counts {
            if j > maxJ {
                maxJ = j
            }
        }
        len := right - left + 1
        if (len - maxJ) > k {
            counts[s[left]]--
            left++
        } else if len > longest {
            longest = len
        }
    }
    return longest
}