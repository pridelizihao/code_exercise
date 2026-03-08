'''
一共n个士兵
每人需要ci次数训练
每人单独训练花费pi元
团购花费S元
所有人训练完需要的总花费最少是多少？
'''
# 输入 n, 人数，S，团购价格
n, S = map(int, input().split())

# tot = pi * ci, 每个人的训练总花费
# 按照训练次数升序排序

nums = [[0,0]] * n

p, c = [0] * n, [0] * n

for i in range(n):
    nums[i] = list(map(int, input().split()))


# 按照nums[i][1]，即训练次数升序排序
nums.sort(key=lambda x: x[1])

for i in range(n):
    p[i] = nums[i][0]
    c[i] = nums[i][1]

# res答案，cnt使用团购的次数，
# total不团购的总花费
res, cnt = 0, 0

tot = sum(p)

for i in range(n):
    if tot >= S:
        res += (c[i] - cnt) * S
        cnt = c[i]
    else:
        res += (c[i] - cnt) * p[i]
    tot -= p[i]

print(res)
