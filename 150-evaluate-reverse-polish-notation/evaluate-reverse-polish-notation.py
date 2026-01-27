# first integers, then the operation to be done on them
# stack
# if integers
    # push into stack
# else
    # pop integers
    # perform op on int
    # push result


# stack = []
# for loop
    # if i.isalphanum()
        # push
    # else:
        # a = pop
        # b = pop
        # stack.append(a i b)
# return stack.pop

from collections import deque
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ops = {'+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '%' : operator.mod,
        '^' : operator.xor}

        for i in tokens:
            if i in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(ops[i](a, b)))
            else:
                stack.append(int(i))
        return stack.pop()