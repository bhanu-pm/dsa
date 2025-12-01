class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0

        ri = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        special = {'I', 'X', 'C'}
        output = 0
        for i in range(len(s)):
            if i+1 < len(s):
                if ri[s[i]] < ri[s[i+1]]:
                    output -= ri[s[i]]
                    continue
            output += ri[s[i]]
        return output