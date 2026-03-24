import sys
input = lambda:sys.stdin.readline().strip()

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

def is_prime(x):
	if x < 2:
		return False
	i = 2
	while i*i <= x:
		if x%i == 0:
			return False
		i += 1
	return True
 
def dfs(start, cnt, s):
	global ans
	
	if cnt == k:
		if is_prime(s):
			ans += 1
		return
	for i in range(start, n):
		dfs(i+1,cnt+1,s+a[i])

dfs(0,0,0)
print(ans)







