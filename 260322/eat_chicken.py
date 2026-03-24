import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())

if n < 10 or n > 30:
	print(0)

else:
	ans = []
	path = [0]*10

	def dfs(pos):
		if pos == 10:
			if s == n:
				ans.append(path[:])
			return
		for i in range(1,4):
			path[pos] = i
			dfs(pos+1,s+i)

	dfs(0,0)

	print(len(ans))
	for p in ans:
		print(*p)
