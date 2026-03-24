from heapq import *
from math import *
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hq = []
        for x in nums:
            heappush(hq,-x)
        res = 0
        for _ in range(k):
            temp = -hq[0]
            res += (-hq[0])
            heappop(hq)
            heappush(hq, -ceil(temp/3))
        return res