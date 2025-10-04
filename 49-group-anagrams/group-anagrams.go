import "sort"

func groupAnagrams(strs []string) [][]string {
    result := [][]string{}
    if len(strs) < 2 {
        result = append(result, strs)
        return result
    }

    sortedStrs := make(map[string][]string)
    for _, str := range strs {
        runes := []rune(str)
        sort.Slice(runes, func(i, j int) bool {
            return runes[i] < runes[j]
        })
        sorted := string(runes)
        sortedStrs[sorted] = append(sortedStrs[sorted], str)
    }

    for _, value := range sortedStrs {
        result = append(result, value)
    }
    return result
}