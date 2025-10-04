import "sort"

func groupAnagrams(strs []string) [][]string {
    result := [][]string{}
    if len(strs) < 2 {
        result = append(result, strs)
        return result
    }

    // sorting methodu
    sortedStrs := make(map[string]string)
    for _, str := range strs {
        runes := []rune(str)
        sort.Slice(runes, func(i, j int) bool {
            return runes[i] < runes[j]
        })
        sorted := string(runes)
        sortedStrs[str] = sorted
    }

    doneIdx := make(map[int]bool)
    for i:=0; i<len(strs); i++ {
        if doneIdx[i] {
            continue
        }

        str := strs[i]
        doneIdx[i] = true
        group := []string{}
        group = append(group, str)

        for j:=0; j<len(strs); j++ {
            // if doneIdx[j] {
            //     continue
            // }
            if i == j {
                continue
            }
            str2 := strs[j]
            if len(str) != len(str2) {
                continue
            }
            if sortedStrs[str] == sortedStrs[str2] {
                group = append(group, str2)
                doneIdx[j] = true
            }
        }
        result = append(result, group)
    }
    return result
}