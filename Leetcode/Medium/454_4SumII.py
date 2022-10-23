from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sums, res = defaultdict(int), 0

        for x in nums1:
            for y in nums2:
                sums[x + y] += 1
                
        for i in nums3:
            for j in nums4:
                res += sums[0 - (i + j)]
                
        return res



nums1 = [-1, -1]
nums2 = [-1, 1]
nums3 = [-1, 1]
nums4 = [1, -1]
target = 0

s = Solution()

print(s.fourSumCount(nums1, nums2, nums3, nums4))
