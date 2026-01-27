# stack
# monotonically decreasing stack
# 5, 4, 3, 2, 2, 1 ...

# input arr of temps
# output = stack.pop()[1] - 

# first only monotonically decreasing stack

from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        output = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if stack:
                while stack and stack[-1][0] < temperatures[i]:
                    # keep popping
                    a, b = stack.pop()
                    output[b] = i-b
                else:
                    stack.append((temperatures[i], i))
            else:
                stack.append((temperatures[i], i))
        
        return output