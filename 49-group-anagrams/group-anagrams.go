func groupAnagrams(strs []string) [][]string {
    result := [][]string{}
    if len(strs) < 2 {
        result = append(result, strs)
        return result
    }

    seen := make(map[string]map[rune]int)

    for _, str := range strs {
        seen[str] = make(map[rune]int)
        for _, letter := range str {
            seen[str][letter]++
        }
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
        
        str2Loop:
        for j:=0; j<len(strs); j++ {
            str2 := strs[j]
            // if doneIdx[j]{
            //     continue
            // }
            if i == j {
                continue
            }
            if len(str) != len(str2) {
                continue
            }
            if str == str2 {
                group = append(group, str2)
                doneIdx[j] = true
            } else {
                for _, letter := range str {
                    if seen[str][letter] != seen[str2][letter] {
                        continue str2Loop
                    }
                }
                group = append(group, str2)
                doneIdx[j] = true
            }
        }
        result = append(result, group)
    }
    return result
}