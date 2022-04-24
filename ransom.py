from itertools import count
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:        
        set_note = set(ransomNote)

        for letter in set_note:
            if ransomNote.count(letter) > magazine.count(letter):
                return False

        return True
        


# Program
t0 = time.perf_counter_ns()

s = Solution()

print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
print(s.canConstruct("aab", "baa"))
print(s.canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
print(s.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")