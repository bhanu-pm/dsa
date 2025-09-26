import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        i = 0
        j = len(lower) - 1

        while i < j:
            if lower[i].isalnum():
                if lower[j].isalnum():
                    if lower[i] == lower[j]:
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