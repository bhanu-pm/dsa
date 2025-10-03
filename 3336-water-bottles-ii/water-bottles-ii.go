func maxBottlesDrunk(numBottles int, numExchange int) int {
    bottlesDrunk := 0
    emptyBottles := 0

    for {
        if emptyBottles >= numExchange {
            emptyBottles -= numExchange
            numBottles += 1
            numExchange += 1
        } else if numBottles > 0 {
            bottlesDrunk += numBottles
            emptyBottles += numBottles
            numBottles = 0
        } else {
            break
        }
    }
    return bottlesDrunk
}