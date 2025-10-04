func groupAnagrams(strs []string) [][]string {
    sortedStrs := make(map[[26]int][]string)
    for _, str := range strs {
        key := [26]int{}
        for _, letter := range str {
            key[letter-'a']++
        }
        sortedStrs[key] = append(sortedStrs[key], str)
    }

    result := make([][]string, 0, len(sortedStrs))
    for _, value := range sortedStrs {
        result = append(result, value)
    }
    return result
}