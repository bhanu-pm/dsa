# input is a string, w only 3 types of brackets
# return bool, about validity of the string

# stack
# store open brackets in stack
# if close bracket of same type as top open bracket in stack
    # pop and its valid
# else
    # return invalid

# dict w '{':'}', '(':')', '[':']'
# for loop
    # if open
        # push into stack
    # else
        # if dict[stack[-1]] == current_bracket:
            # stack pop
            # valid
        # else
            # return False
# return True

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        brackets = {'{':'}', '(':')', '[':']'}

        for i in s:
            # open bracket
            if i in brackets:
                stack.append(i)
            # closed
            else:
                if stack:
                    if brackets[stack.pop()] == i:
                        continue
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        return True