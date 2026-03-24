import sys
input = sys.stdin.readline().strip()

a, b, c = map(int, input().split())

ans = []

for k in range(1,1000):
	A = a*k
	B = b*k
	C = c*k

	if A<100 or B<100 or C<100:
		continue
	if A>999 or B>999 or C>999:
		break
	
	s = str(A) + str(B) + str(C)
	
	if '0' in s:
		continue
	if len(set(s)) == 9:
		ans.append((A,B,C))

if not ans:
	print("No!")
else:
	for x in ans:
		print(*x)
