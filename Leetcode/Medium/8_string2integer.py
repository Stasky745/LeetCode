import time

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        res = 0
        sign = 1
        
        if len(s) == 0:
            return 0
        
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            
            s = s[1:]
            
        while len(s) > 0 and s[0].isnumeric():
            res = res * 10 + int(s[0])
            
            if not (-2**31 <= res * sign and res * sign < 2**31):
                if sign > 0:
                    return 2**31 - 1
                else:
                    return -2**31
            
            s = s[1:]
               
               
        return res * sign
                    


# Program
x1 = "42"
x2 = "-42"
x3 = "      42"
x4 = "4192 with words"
x5 = "-91283472332"

t0 = time.perf_counter_ns()

s = Solution()

print(s.myAtoi(x1))
print(s.myAtoi(x2))
print(s.myAtoi(x3))
print(s.myAtoi(x4))
print(s.myAtoi(x5))

t1 = time.perf_counter_ns()

print(f"{(t1 - t0) / 1000000} ms.")
