from colllections import deque

q = deque()
g[3][4] = 0
di = [(0,1),(0,-1),(1,0),(-1,0)]

while q:
	x,y = q.popleft()
	for dx,dy in di:
		nx, ny = x+dx,y+dy
		if 0<=nx<n and 0<=ny<m:
			q.append((nx,ny))
			g[nx,ny] = 0

