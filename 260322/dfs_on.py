import sys
input = lambda:sys.stdin.readline().strip()
sys.setrecursionlimit(10000)
n = int(input())
g = [0] + list(map(int, input().split()))
res = 0
d = {}

def dfs(u,idx):
	global res
	if d.get(u) is not None:
		res = max(res,idx - d[u])
		return
	d[u] = idx
	dfs(g[u],idx+1)
for u in range(1,n+1):
	dfs(u,1)

print(res)
