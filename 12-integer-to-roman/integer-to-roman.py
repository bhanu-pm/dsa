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
        special = {5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        while num > 0:
            if num < 4:
                result.append('I')
                num -= 1
            elif num == 4:
                result.append('I')
                num += 1
            elif num == 5:
                result.append('V')
                num = 0
            elif num < 9:
                result.append('V')
                num -= 5
            elif num == 9:
                result.append('I')
                num += 1
            elif num == 10:
                result.append('X')
                num = 0
            elif num < 40:
                result.append('X')
                num -= 10
            elif num == 40:
                result.append('X')
                num += 10
            elif num < 50:
                result.append('X')
                num += 10
            elif num == 50:
                result.append('L')
                num = 0
            elif num < 90:
                result.append('L')
                num -= 50
            elif num == 90:
                result.append('X')
                num += 10
            elif num < 100:
                result.append('X')
                num += 10
            elif num == 100:
                result.append('C')
                num = 0
            elif num < 400:
                result.append('C')
                num -= 100
            elif num == 400:
                result.append('C')
                num += 100
            elif num < 500:
                result.append('C')
                num += 100
            elif num == 500:
                result.append('D')
                num = 0
            elif num < 900:
                result.append('D')
                num -= 500
            elif num == 900:
                result.append('C')
                num += 100
            elif num < 1000:
                result.append('C')
                num += 100
            elif num == 1000:
                result.append('M')
                num = 0
            elif num < 4000:
                result.append('M')
                num -= 1000
            else:
                break
        
        return ''.join(result)