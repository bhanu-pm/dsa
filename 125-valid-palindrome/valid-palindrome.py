import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i < j:
            i_char = s[i]
            j_char = s[j]
            if i_char.isalnum():
                if j_char.isalnum():
                    if i_char == j_char:
                        i += 1
                        j -= 1
                        pass
                    else:
                        return False
                else:
                    j -= 1
            else:
                i += 1
        else:
            return True