n, S = map(int, input().split())

nums = [[0,0]] * n

p, c = [0]*n, [0]*n

for i in range(n):
    nums[i] = list(map(int, input().split()))

nums.sort(key=lambda x: x[1])

for i in range(n):
    p[i] = nums[i][0]
    c[i] = nums[i][1]

res, cnt = 0, 0

total = sum(p)

for i in range(n):
    if total >= S:
        res += (c[i] - cnt) * S
        cnt = c[i]
    else:
        res += (c[i] - cnt) *p[i]
    total -= p[i]

print(res)
