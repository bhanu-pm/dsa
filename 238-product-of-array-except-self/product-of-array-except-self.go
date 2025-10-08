func productExceptSelf(nums []int) []int {
    length := len(nums)
    result := make([]int, length)
    preproduct := 1
    postproduct := 1
    j := length-1
    for i:=0; i<length; i++ {
        if i<j {
            result[i] = preproduct
            preproduct *= nums[i]
    
            result[j] = postproduct
            postproduct *= nums[j]
        } else if i==j {
            result[i] = preproduct
            preproduct *= nums[i]
    
            result[j] *= postproduct
            postproduct *= nums[j]
        } else {
            result[i] *= preproduct
            preproduct *= nums[i]
    
            result[j] *= postproduct
            postproduct *= nums[j]
        }
        j--
    }
    return result
}