#  - Open brackets should be closed by the same type.
#  - correct order
#  - every open bracket has a corresponding close brack and vice versa.

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        closed = {"}":"{", ")":"(", "]":"["}
        stack = deque()
        for i in s:
            if i in closed: # closed bracket
                if stack:
                    openb = stack.pop()
                    if closed[i] == openb:
                        continue
                    else:
                        return False
                else:
                    return False
            else: # open bracket
                stack.append(i)
        if stack:
            return False
        return True
        