import time
from typing import List
'''

'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Assuming both lists aren't empty
        N1, N2 = len(nums1), len(nums2)
        
        if N1 > N2:
            return self.findMedianSortedArrays(nums2, nums1)            # Make sure nums1 is the shorter one
        
        '''
        Now Binary Search
        '''
        start = 0
        end = N1
        midMergedArray = (N1 + N2 + 1) // 2
        
        while start <= end:
            cut = (start + end) // 2                         # Calculate the cut (done on Nums1)
            leftSize1 = cut                                  # Left size of Nums1
            leftSize2 = midMergedArray - leftSize1           # Left size of Nums2
            
            # Get L1, R1, L2, R2
            L1 = nums1[leftSize1-1]   if   leftSize1 > 0     else    float("-inf")
            L2 = nums2[leftSize2-1]   if   leftSize2 > 0     else    float("-inf")
            R1 = nums1[leftSize1]     if   leftSize1 < N1    else    float("inf")
            R2 = nums2[leftSize2]     if   leftSize2 < N2    else    float("inf")
            
            if L1 > R2:
                end = cut - 1               # Nums1's left side is too big; need to move the cut left
            elif L2 > R1:
                start = cut + 1             # Nums2's left side is too big; need to move the cut right (equivalent to moving a cut in Nums2 to the left)
            else:
                # Even length of total items; the biggest of the lefts and smallest of the rights are the values around the median
                if (N1 + N2) % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                
                # Odd length of total items; the biggest of the lefts is the median
                return max(L1, L2)
        
        return -1
            
    
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