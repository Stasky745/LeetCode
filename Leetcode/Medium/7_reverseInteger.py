import time

class Solution:
    def reverse(self, x: int) -> int:
        limit = 2147483648
        nLimit = len(str(limit))
        
        neg = False
        if x < 0:
            neg = True
            x *= -1
            
        # 2^31 = 2147483648
        # for it to be larger than this it has to have at least the same amount of digits (> 1000000000)
        overflow = True
        if x <= 1000000000 or x % 10 == 0:
            overflow = False
            
        res = 0
            
        while x > 0:
            # we get the last digit
            y = x % 10
            
            # we make x shorter
            x = x // 10
            
            # we add y to the result
            res = res * 10 + y
            
            if overflow:
                if neg and res < limit // (10 ** (nLimit - len(str(res)))):
                    overflow = False
                elif not neg and res < (limit-1) // (10 ** (nLimit - len(str(res)))):
                    overflow = False
           
        if overflow:
            return 0
        
        if neg:
            return res * -1
        
        return res
                    
                    


# Program
x1 = 123
x2 = -123
x3 = 120
x4 = 1563847412

t0 = time.perf_counter_ns()

s = Solution()

print(s.reverse(x1))
print(s.reverse(x2))
print(s.reverse(x3))
print(s.reverse(x4))

t1 = time.perf_counter_ns()

print(f"{(t1 - t0) / 1000000} ms.")
