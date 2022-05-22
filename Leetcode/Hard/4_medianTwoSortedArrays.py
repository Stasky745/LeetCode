import time
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Find out where the middle of the total list will be
        l1, l2 = len(nums1), len(nums2)
        
        '''
        This following call is to only take into consideration when nums1 is smaller than nums2, so we don't write double the code
        '''
        if (l1 > l2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        '''
        Now Binary Search
        '''
        # we find the middle
        middle = (l1 + l2 - 1) // 2
        # we define pointers
        left, right = 0, l1
        
        while left < right:
            mid1 = (left + right) // 2
            mid2 = middle - mid1
            
            if nums1[mid1] < nums2[mid2]:
                left = mid1 + 1
            else:
                right = mid1
                
        '''
        After the binary search we know the median must be between these 4 numbers:
         - nums1[ left - 1 ]
         - nums1[ left ]
         - nums2[ middle - left]
         - nums2[ middle - left + 1]
        '''
        
        '''
        if (l1+l2) is odd, the median is the bigger one between:
         - nums1[ left - 1 ]
            and
         - nums2[ middle - left ]
        With some corner cases
        '''
        # We find which one would be the solution
        aux1 = nums1[left - 1] if left > 0 else -1
        aux2 = nums2[middle-left] if middle-left >= 0 else -1
        
        res1 = max(aux1, aux2)
            
        # Return it if it's an odd length
        if (l1+l2) % 2 == 1:
            return res1
        
        
        '''
        if (l1+l2) is even, the median is:
            median = (res1 + min(nums1[left], nums2[ middle - left + 1 ]) / 2
        '''
        # We find which is the second part we need
        aux1 = nums1[left] if left < l1 else float("inf")
        aux2 = nums2[middle - left + 1] if middle - left + 1 < l2 else float("inf")
        res2 = min(aux1, aux2)
        
        return (res1 + res2) / 2
    
# Program
s1 = [1,3]
p1 = [2]

s2 = [1,2]
p2 = [3,4]

t0 = time.perf_counter_ns()

s = Solution()

print(s.findMedianSortedArrays(s1, p1))
print(s.findMedianSortedArrays(s2, p2))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")    