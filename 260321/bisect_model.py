def bisect(a, x, lo = 0, hi = None):
	if hi is None: hi = len(a)
	while lo < hi:
		i = (lo+hi) >> 1
		if a[i] > x:
			hi = i
		else:	
			lo = i+1
	return lo

a = [1,9,9,9,200,500]

print(bisect(a,9))
print(bisect(a,1000))
