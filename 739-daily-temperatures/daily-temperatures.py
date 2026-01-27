
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if stack:
                while stack and temperatures[i] > stack[-1][0]:
                    a, b = stack.pop()
                    output[b] = i-b
            stack.append((temperatures[i], i))

        return output