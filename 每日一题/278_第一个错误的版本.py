# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

"""
LeetCode 278: 第一个错误的版本 (First Bad Version)

问题描述:
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

解题思路:
这是一个典型的二分查找问题。版本号从1到n，其中有一个分界点：
- 所有在分界点之前的版本都是好的 (isBadVersion(version) == False)
- 所有在分界点及之后的版本都是坏的 (isBadVersion(version) == True)
我们需要找到这个分界点，即第一个返回 True 的版本。

算法分析:
使用二分查找在区间 [1, n] 中搜索：
1. 如果中间版本是坏的 (isBadVersion(mid) == True):
   - 检查前一个版本 mid-1 是否是好的
   - 如果前一个版本是好的，那么 mid 就是第一个坏版本
   - 如果前一个版本也是坏的，说明第一个坏版本在左半部分，缩小搜索范围到 [left, mid-1]
2. 如果中间版本是好的 (isBadVersion(mid) == False):
   - 说明第一个坏版本在右半部分，缩小搜索范围到 [mid+1, right]

时间复杂度: O(log n)，每次将搜索范围减半
空间复杂度: O(1)，只使用了常数级别的额外空间

边界情况处理:
- 当 mid == 1 时，直接返回 1（第一个版本就是坏的）
- 当 left > right 时循环结束（但本题保证存在坏版本，所以不会出现这种情况）
"""

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 初始化搜索区间为 [1, n]
        left = 1
        right = n
        
        # 二分查找循环
        while left <= right:
            # 计算中间版本号，使用整数除法避免溢出
            mid = (left + right) // 2
            
            # 检查中间版本是否是坏的
            if isBadVersion(mid):
                # 如果中间版本是第一个版本 (mid == 1)，直接返回1
                if mid == 1:
                    return 1
                else:
                    # 检查前一个版本是否是好的
                    if isBadVersion(mid - 1):
                        # 前一个版本也是坏的，说明第一个坏版本在左半部分
                        # 缩小搜索范围到 [left, mid-1]
                        right = mid - 1
                    else:
                        # 前一个版本是好的，当前版本是第一个坏的
                        return mid
            else:
                # 中间版本是好的，说明第一个坏版本在右半部分
                # 缩小搜索范围到 [mid+1, right]
                left = mid + 1
        
        # 理论上不会执行到这里，因为题目保证存在坏版本
        # 但为了代码完整性，返回 left（此时 left > right）
        return left


                
