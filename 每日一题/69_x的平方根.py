class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        return int(math.sqrt(x))


s1 = Solution()

num1 = s1.mySqrt(15)
print(num1)
