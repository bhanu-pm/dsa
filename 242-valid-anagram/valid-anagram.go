func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    seenS := make(map[rune]int)
    seenT := make(map[rune]int)

    for _, letter := range s {
        seenS[letter]++
    }
    for _, letter := range t {
        seenT[letter]++
    }

    for letter, num := range seenS {
        if seenT[letter] != num {
            return false
        }
    }
    return true
}