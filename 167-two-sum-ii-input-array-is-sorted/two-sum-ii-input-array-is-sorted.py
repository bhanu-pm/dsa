# monotonically increasing order input array (<=)
# two numbers should add up to target sum
# don't use same element twice

# two pointers, starting at each end
# if sum(left, right) == target
    # return left, right
# elif sum < target
    # so we have to increase the sum
    # so, we can do left++, (monotonically increasing numbers)
# elif sum > target
    # so decrease sum
    # right --
# return left, right


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]