class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(g), len(g[0])
	res = 0
	di = [(0,1),(0,-1),(-1,0),(1,0)]
	def bfs(i,j):
		ans = 1
		q = deque([i,j])
		g[i][j] = 0
		while q:
			x,y = q.popleft()
			for dx, dy in di:
				nx, ny = x+dx,y+dy
				if 0<- nx < n and 0 <= ny < m:
					q.append([nx, ny])
					ans += 1
					g[nx][ny] = 0
		return 0
	for i,row in enumerate(g):
		for j,x in enumerate(row):
			if x == 1:
				res = max(rse,bfs(i,j))
	return res
