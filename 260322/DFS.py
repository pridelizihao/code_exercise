import sys

input = lambda: sys.stdin.readline().strip()
N,A,B = map(int, input().split())
sN = str(N)
res = 0

def dfs(i,n,a,b)
	global res
	if i >= len(sN):
		res = max(res,n)
		return
	x = int(sN[i])
	d = min(9-x,a)
	dfs(i+1,n*10+(x+d),a-d,b)
	if b >= x+1:
		dfs(i+1,n*10+9,a,b(x+1))

dfs(0,0,A,B)
print(res)

