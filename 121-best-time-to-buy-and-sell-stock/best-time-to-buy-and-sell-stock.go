func maxProfit(prices []int) int {
    min := 9999
    output := 0

    for _, today := range prices{
        diff := today - min

        if diff > output{
            output = diff
        }

        if min > today{
            min = today
        }
    }
    return output
}