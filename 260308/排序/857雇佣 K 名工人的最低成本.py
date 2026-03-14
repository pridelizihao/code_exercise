from heapq import heappush, heappop
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        nums = sorted([(w/q,q) for w,q in zip(wage,quality)])
        
        hq,s = [], 0
        for i in range(k):
            heappush(hq, -nums[i][1])
            s += nums[i][1]
        res = nums[k-1][0] * s

        for i in range(k,n):
            mxw = -heappop(hq)
            s -= mxw
            mxw = min(mxw, nums[i][1])
            heappush(hq, -mxw)
            s += mxw
            res = min(res, nums[i][0] *s)
        return res
