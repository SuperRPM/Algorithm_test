import sys

input = sys.stdin.readline
import heapq

pop = heapq.heappop
push = heapq.heappush

n = int(input())
schedule = []

for _ in range(n):
    p, t = map(int, input().split())
    schedule.append((t, p))
schedule.sort(key=lambda x: x[0])

total_pay = []

for day_pay in schedule:
    push(total_pay, day_pay[1])
    if len(total_pay) > day_pay[0]:
        pop(total_pay)

print(sum(total_pay))
'''
3
100 2
50 2
30 1
'''