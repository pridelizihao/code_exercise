import sys
input = lambda:sys.stdin.readline().strip()

n, m, p = map(int, input().split())

fa = list(range(n+1))
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]
def union(u, v):
    if find(u) != find(v):
        fa[find(u)] = find(v)

for _ in range(m):
    u,v = map(int, input().split())
    union(u,v)

for _ in range(p):
    u,v = map(int, input().split())
    if find(u) == find(v):
        print("Yes")
    else:
        print("No")