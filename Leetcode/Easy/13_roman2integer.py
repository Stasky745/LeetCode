import time
from typing_extensions import Self

class Solution(object):
    def romanToInt(self, s) -> int:
        # Map with the value of each letter
        dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        # The result of the String + The value of the letter before the current one
        result, last_value = 0, 0
        
        # We go reverse, from the last letter to the first
        for char in reversed(s):
            # We get the value of the current letter
            current_value = dict[char]
                    
            # If the last value was bigger, means that current value is used to subtract. Otherwise we add
            if(last_value > current_value):
                result -= current_value
            else:
                result += current_value
            
            # We update the value
            last_value = current_value
                    
        return result

t0 = time.perf_counter_ns()

s1 = Solution()

print(s1.romanToInt("III"))
print(s1.romanToInt("LVIII"))
print(s1.romanToInt("MCMXCIV"))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")