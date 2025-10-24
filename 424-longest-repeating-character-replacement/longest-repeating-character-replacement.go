func characterReplacement(s string, k int) int {
    longest := 0
    left := 0
    maxJ := 0
    counts := make(map[rune]int)

    for right, letter := range s {
        counts[letter]++
        if counts[letter] > maxJ {
            maxJ = counts[letter]
        }
        len := right - left + 1
        if (len - maxJ) > k {
            counts[rune(s[left])]--
            left++
        } else if len > longest {
            longest = len
        }
    }
    return longest
}