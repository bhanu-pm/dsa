func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    seen := make(map[rune]int)

    for _, letter := range s {
        seen[letter]++
    }
    for _, letter := range t {
        if seen[letter] == 0 {
            return false
        }
        seen[letter]--
    }
    return true
}