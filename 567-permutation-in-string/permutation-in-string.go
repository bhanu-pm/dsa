func checkInclusion(s1 string, s2 string) bool {
    dict := make(map[byte]int, len(s1))
    dict2 := make(map[byte]int, len(s2))
    i := 0
    j := len(s1)
    for a, _ := range s1 {
        dict[s1[a]]++
    }
    for j<=len(s2) {
        if _, ok := dict[s2[i]]; ok {
            clear(dict2)
            for b, _ := range s2[i:j] {
                dict2[s2[i+b]]++
            }
            if maps.Equal(dict, dict2) {
                return true
            }
        }
        i++
        j++
    }
    return false
}