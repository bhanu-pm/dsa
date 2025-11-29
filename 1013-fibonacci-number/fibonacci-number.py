class Solution:
    # def __init__(self):
    #     self.mem = [0, 1]
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        fn = self.fib(n-1) + self.fib(n-2)
        return fn