import sys
import os

from collections import *
input = lambda:sys.stdin.readline().strip()


n, m = map(int,input().split())
g = [[0] * m for _ in range(n)]
di = [(0,1),(0,-1),(1,0),(-1,0)]
q = deque()

for i in range(n):
	r = input()
	for j,x in enumerate(r):
		if x == "g":
			g[i][j] = 1
			q.append((i,j))

k = int(input())
while q and k:
	for _ in range(len(q)):
		x,y = q.popleft()
		for dx,dy in di:
			nx, ny = x+dx,y+dy
 			if 0 <= nx < n and 0<= ny < m and g[nx][ny]==0:
				g[nx][ny] = 1
				q.append((nx,ny))
	k = k-1

"""
for row in g:
	for x in row:
		if x == 1:
			print("g",end="")
		else:
			print(".",end="")
	print()
"""
for row in g:
	print("".join("g" if x else "." for x in row))
