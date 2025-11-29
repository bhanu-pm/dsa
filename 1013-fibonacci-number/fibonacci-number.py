class Solution:
    def __init__(self):
        self.mem = [0, 1, 1]
        self.len = 2
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        if n < self.len:
            return self.mem[n]
        
        fn = self.fib(n-1) + self.fib(n-2)
        self.mem.append(fn)
        self.len += 1
        return fn