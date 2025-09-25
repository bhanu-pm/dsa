class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        for num in numbers:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i+1, j+1]
            
            if total < target:
                i += 1
            else:
                j -= 1

            if i == j:
                return [-1, -1]
