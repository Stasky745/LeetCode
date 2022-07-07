import time

class Solution:
    def isNumber(self, s: str) -> bool:
        return self.isValid(s.lower())
    
    
    def isValid(self, n: str) -> bool:
        if n.isnumeric():
            return True
        
        if len(n) == 0 or n[0] == 'e':
            return False
        
        valid = n.split('e')
        
        if len(valid) > 2:
            return False
        
        if not self.isDecimal(valid[0]):
            return False 
        
        if len(valid) == 2:
            if not self.isInteger(valid[1]):
                return False 
            
        return True
    
    
    def isDecimal(self, n: str) -> bool:        
        if n.isnumeric():
            return True
        
        if len(n) == 0:
            return False
        
        if n[0] in ['+','-']:
            n = n[1:]
            
        decimal = n.split('.')
        
        if len(decimal) == 1:
            return True if self.isInteger(decimal[0]) else False
        
        if len(decimal) == 2:
            if decimal[0] == '' and decimal[1] == '':
                return False
            
            if decimal[0] != '' and not self.isInteger(decimal[0]):
                return False
            
            if decimal[1] != '' and not decimal[1].isnumeric():
                return False
            
            return True
        
        return False
            

    def isInteger(self, n: str) -> bool:
        if n.isnumeric() or (len(n) > 0 and n[0] in ['+', '-'] and n[1:].isnumeric()):
            return True
        
        return False
                    


# Program
x1 = "0"
x2 = "e"
x3 = "i.1"
x4 = ".3"
x5 = "0e"

t0 = time.perf_counter_ns()

s = Solution()

print(s.isNumber(x1))
print(s.isNumber(x2))
print(s.isNumber(x3))
print(s.isNumber(x4))
print(s.isNumber(x5))

t1 = time.perf_counter_ns()

print(f"{(t1 - t0) / 1000000} ms.")
