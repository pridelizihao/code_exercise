from heapq import *
hq = []

heappush(hq, 5)
heappush(hq, 9)
heappush(hq, 11)
heappush(hq, 12)
heappush(hq, 13)
heappush(hq, 15)
print(hq)

print(hq[0])
heappop(hq)
print(hq)

nums = [15,13,9,5,11,12]
hq = []

for x in nums:
    heappush(hq, -x)

print(hq)

print(-hq[0])

heappop(hq)
print(hq)

print(-hq[0])

