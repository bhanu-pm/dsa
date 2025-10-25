func checkInclusion(s1 string, s2 string) bool {
    if len(s1) > len(s2) {
        return false
    }
    dict := make(map[byte]int, len(s1))
    dict2 := make(map[byte]int, len(s2))
    j := len(s1)-1
    for a := range s1 {
        dict[s1[a]]++
    }
    for b := range s2[0:j] {
        dict2[s2[b]]++
    }
    for i:=0; j<len(s2); i++ {
        dict2[s2[j]]++
        if maps.Equal(dict, dict2) {
            return true
        }
        dict2[s2[i]]--
        if dict2[s2[i]] == 0 {
            delete(dict2, s2[i])
        }
        j++
    }
    return false
}