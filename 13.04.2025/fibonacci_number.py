class Solution:
    def fib(self, n: int) -> int:
        fib = [0,1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            f1, f2 = fib[0], fib[1]
            for j in range(1,n+1):
                fib.append(f1 + f2)
                f1, f2 = f2, (f1  + f2)
            return fib[n]
        
