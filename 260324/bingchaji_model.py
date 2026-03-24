import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
fa = list(range(n+1))

def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

def union(u, v):
    if find(u) != find(v):
        fa[find(u)] = find(v)