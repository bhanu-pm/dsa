func characterReplacement(s string, k int) int {
    longest := 0
    left := 0
    maxCount := 0
    countDict := make(map[rune]int)

    for right, char := range s {
        countDict[char]++
        if countDict[char] > maxCount{
            maxCount = countDict[char]
        }

        windowLen := right - left + 1
        if (windowLen - maxCount) > k {
            countDict[rune(s[left])]--
            left++
        } else if windowLen > longest {
            longest = windowLen
        }
    }
    return longest
}