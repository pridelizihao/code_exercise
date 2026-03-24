import os
import sys

# 请在此输入您的代码

input = lambda: sys.stdin.readline().strip()

n = int(input())

lst = []
for _ in range(n):
  lst_temp = list(map(int, input().split()))
  lst.append(lst_temp)

a,b = zip(*lst)

def bisect(lo,hi,check):
  while lo < hi:
    i = (lo+hi)//2
    if check(i):
      hi = i
    else:
      lo = i+1
  return lo

def ok_lower(v):
	return all(A//v  <= B for A,B in zip(a,b))

def ok_upper(v):
    return any(A // v < B for A, B in zip(a, b))
m = bisect(1,10**9,ok_lower)
M = bisect(1,10**9,ok_upper)

print(m,M)
