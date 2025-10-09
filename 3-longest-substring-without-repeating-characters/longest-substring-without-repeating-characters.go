func lengthOfLongestSubstring(s string) int {
    seen := make(map[rune]int)
    maxlen := 0
    i := 0

    for j, letter := range s {
        if result, ok := seen[letter]; ok && result >= i {
            i = result + 1
        }
        seen[letter] = j
        length := j - i + 1
        if length > maxlen {
            maxlen = length
        }
    }
    return maxlen
}