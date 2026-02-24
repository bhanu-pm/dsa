# array of temps
# return answer arr

# answer arr
    # answer[i] = no. of days to wait after i'th day, to get a warmer temp.
    # if no warmer future day, answer[i] = 0

# monotonically decreasing stack
    # this stack stores a value

    # if we get a colder day
        # we store it, index value
    # while stack.top < new day
        # we pop the stack
        # j-i and store it in i'th index
# return answer

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for j, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                i, s_temperature = stack.pop()
                answer[i] = j-i

            stack.append((j, temperature))
        return answer