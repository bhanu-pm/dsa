func groupAnagrams(strs []string) [][]string {
    result := [][]string{}
    if len(strs) < 2 {
        result = append(result, strs)
        return result
    }

    sortedStrs := make(map[[26]int][]string)
    for _, str := range strs {
        key := [26]int{}
        for _, letter := range str {
            key[letter-'a']++
        }
        sortedStrs[key] = append(sortedStrs[key], str)
    }

    for _, value := range sortedStrs {
        result = append(result, value)
    }
    return result
}