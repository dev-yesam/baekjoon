import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s, 1))  # 시작점
    lst.append((e, -1))  # 끝점

lst.sort(key=lambda x: (x[0], x[1]))
ans_lst = []
ans = 0
count = 0
for x, y in lst:
    if y == 1 : # 시작점이면
        count+=1
        ans = max(ans,count)
    else: # 끝점이면
        count -= 1

print(ans)