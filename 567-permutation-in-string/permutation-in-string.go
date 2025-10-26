func checkInclusion(s1 string, s2 string) bool {
    if len(s1) > len(s2) {
        return false
    }
    dict1 := make(map[byte]int)
    dict2 := make(map[byte]int)
    i:=0
    for b := range s1 {
        dict1[s1[b]]++
    }
    for a:=0; a<len(s1)-1; a++ {
        dict2[s2[a]]++
    }

    for j:=len(s1)-1; j<len(s2); j++ {
        dict2[s2[j]]++
        if maps.Equal(dict1, dict2) {
            return true
        }
        dict2[s2[i]]--
        if dict2[s2[i]] == 0 {
            delete(dict2, s2[i])
        }
        i++
    }
    return false
}