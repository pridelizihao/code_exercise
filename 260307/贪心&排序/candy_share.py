"""
老师给学生发糖果
每人偶数个
小朋友把自己的一半分给左手的孩子
奇数个的老师补发一个
反复进行，直到所有人的数目相同
文，以知的情况下，需要补多少个

"""
import sys
input= lambda: sys.stdin.readline().strip()

# n个学生，每人一个初始的糖果数
n = int(input())
nums = list(map(int, input().split()))
a = sum(nums)

while True:
    nums1 = nums.copy()
    for i,x in enumerate(nums):
        # 自己的一半加上右边孩子的一半
        nums1[i] = (x // 2) + (nums[(i+1)%n] // 2)
        if nums1[i] % 2 == 1:
            nums1[i] += 1
    nums = nums1
    if len(set(nums)) == 1:
        break

print(sum(nums) - a)