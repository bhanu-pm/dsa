func longestConsecutive(nums []int) int {
    // Put all numbers on our "magic table" for O(1) lookups.
    // This is O(n).
    numSet := make(map[int]bool)
    for _, num := range nums {
        numSet[num] = true
    }

    longestStreak := 0

    // O(n) pass to check each number.
    for num := range numSet {
        // IMPORTANT: Is this number the start of a sequence ("engine")?
        // We only check if the number just before it is NOT in the set.
        if !numSet[num-1] {
            currentNum := num
            currentStreak := 1

            // This inner loop only runs for numbers that are part of a sequence,
            // and since we start from an engine, each number is only ever
            // visited once here across the entire execution.
            for numSet[currentNum+1] {
                currentNum++
                currentStreak++
            }

            // Update the longest streak found so far.
            if currentStreak > longestStreak {
                longestStreak = currentStreak
            }
        }
    }

    return longestStreak
}