# input arr of temps
# if no soln. answer[i] = 0
# so init arr with 0s

# monotonically decreasing stack first

# if no element in stack
    # push into stack
# else
    # while stack and curr > stack[-1]
        # popped = stack pop()
        # it means we found the next big element
        # output[poppped[1]] = curr_idx - popped[1]
    # else
        # push into stack
# return output

from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    a, b = stack.pop()
                    output[b] = i-b
                else:
                    stack.append((temperatures[i], i))
        return output