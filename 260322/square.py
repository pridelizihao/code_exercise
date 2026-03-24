import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())

lim = min(n,m)
square = 0
for k in range(1,lim+1):
	square += (n-k+1)*(m-k+1)

rect_total =  (n+1)*n//2*(m+1)*m//2
rect_only = rect_total-square

print(square,rect_only)


