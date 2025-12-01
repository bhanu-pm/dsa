class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        sol = ""
        maxlen = 0

        for i in range(len(s)):
            # odd lengthed palindrome
            l, r = i, i
            while (l >= 0 and r < len(s)) and (s[l] == s[r]):
                if (r-l+1) > maxlen:
                    maxlen = r-l+1
                    sol = s[l:r+1]
                l -= 1
                r += 1
            
            # even lengthed palindrome
            l, r = i, i+1
            while (l >= 0 and r < len(s)) and (s[l] == s[r]):
                if (r-l+1) > maxlen:
                    maxlen = r-l+1
                    sol = s[l:r+1]
                l -= 1
                r += 1
            
        return sol