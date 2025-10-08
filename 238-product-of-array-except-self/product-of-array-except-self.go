func productExceptSelf(nums []int) []int {
    result := make([]int, len(nums))
    product := 1
    for i:=0; i<len(nums); i++ {
        if i>0 {
            product *= nums[i-1]
            result[i] = product
        } else {
            result[i] = 1
        }
    }

    product = 1
    for j:=len(nums)-1; j>=0; j-- {
        if j < len(nums)-1{
            product *= nums[j+1]
            result[j] *= product
        }
    }
    return result
}