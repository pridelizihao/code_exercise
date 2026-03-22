from bisect import *
a = []
lower = int(input())
upper = int(input())

a.sort()
res = 0
for i,x in enumerate(a):
	L = bisect(a, lower-x-1,i+1)
	R = bisect(a, upper-x, i+1) - 1
	res = R-L+1

print(res)
