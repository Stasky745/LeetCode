import time
from typing import List

class Solution(object):
    def fizzBuzz(self, n: int) -> List[str]:
        for i in range(1, n+1):
            item = ''
            
            if i % 3 == 0:
                item += 'Fizz'
            if i % 5 == 0:
                item += 'Buzz'
            elif item == '':
                item = str(i)
            
            yield item
        
        


# Program
t0 = time.perf_counter_ns()

s = Solution()

print(list(s.fizzBuzz(3)))
print(list(s.fizzBuzz(5)))
print(list(s.fizzBuzz(15)))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")