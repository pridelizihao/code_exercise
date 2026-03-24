import sys
input = lambda:sys.stdin.readline().strip()

while True:
    s = input()
    if s == '0': break
    n, m = map(int, s.split())
    fa = list(range(n+1))
    def find(x):
        if fa[x] != x:
            return find(fa[x])
        return fa[x]
    def union(u,v):
        if find(u) != find(v):
            fa[find(u)] = find(v)
    for _ in range(m):
        u,v = map(int, input().split())
        union(u,v)

    for x in range(1,n+1):
        fa[x] = find(x)

    cnt = len(set(fa)) - 1
    print(cnt-1)
        