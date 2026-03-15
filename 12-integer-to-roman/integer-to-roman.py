# ordered dict with all special values

# while loop
    # subtract biggest possible number in dict from input


class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        od = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

        for i in od.keys():
            while num >= i:
                result.append(od[i])
                num -= i
        return ''.join(result)