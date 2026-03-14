import sys
input = lambda: sys.stdin.readline().strip()

n,m = map(int, input().split())
cnt = [0] * (n+1)

for x in map(int, input().split()):
    cnt[x] += 1 

for i in range(1, n+1):
    print((str(i)+" ") * cnt[i],end="")