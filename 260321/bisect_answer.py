class Solution:
	def maxmumCandies(self, a: List[int], k: int) -> int:
		if sum(a) < k: return 0
		lo, hi= 1, 10**12+10
		def check(res):
			return sum(x // res for x in a) < k
		while lo < hi:
			i = (lo + hi) >> 1
			if check(i): hi = i
			else:
				lo = i+1
		return lo - 1
		
