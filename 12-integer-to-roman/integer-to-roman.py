# if value ! 4 or 9
    # select max symbol < input
    # input -= max symbol

# if 4 or 9
    # go to subtractive mode
    # 4 = I - V
    # 9 = I - X

# only the following subtractive forms are used
# 4, 9, 40, 90, 400, 900

# powers of 10 (I, X, C, M) can be appended at max 3 times
    # if 4 or 9, go to sub mode

# 5, 50, 500 cannot be appended multiple times

# num <= 3999

class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        int_roman = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]

        for i in int_roman:
            while num >= i[0]:
                result.append(i[1])
                num -= i[0]
        
        return ''.join(result)