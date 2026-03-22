def f(x):
	return x**3+ x +1

def bisect(lo, hi, target,check):
	while lo < hi:
		i = (lo + hi) >> 1
		if check(i, target):
			hi = i
		else:
			lo = i+1
	return lo

target = 99999
res = bisect(1,10**18, target, lambda y, target:f(y) > target)
print(res)
print(f(res))
print(f(res-1))
