import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())

a = list(map(int, input().split()))

q = int(input())



p = [0] * (n+1)
for i in range(n):
    p[i+1] = p[i] + a[i]

for _ in range(q):
    l, r = map(int, input().split())
    ans = p[r] - p[l-1]
    print(ans)
