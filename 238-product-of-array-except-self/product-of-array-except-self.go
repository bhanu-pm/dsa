func productExceptSelf(nums []int) []int {
    length := len(nums)
    result := make([]int, length)
    product := 1
    for i:=0; i<length; i++ {
        result[i] = product
        product *= nums[i]
    }

    product = 1
    for j:=length-1; j>=0; j-- {
        result[j] *= product
        product *= nums[j]
    }
    return result
}