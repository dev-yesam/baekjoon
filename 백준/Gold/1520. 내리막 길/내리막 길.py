# 240407
# BFS + 최대힙 + DP 로 풀 수 있을 듯.

from collections import deque
from heapq import heappush, heappop

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블
dt = [[0] * m for _ in range(n)]


# BFS
def bfs(r, c):
    # 시작점
    dt[0][0] = 1
    heap = []
    heappush(heap, (arr[0][0] * -1, r, c)) # 최대힙

    # 방문 예약 탐색
    while heap:
        # 꺼내기
        height, cr, cc = heappop(heap)
        height *= -1

        # 다음 방문
        for nr, nc in ((cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)):
            # 범위 내고, 높이가 지금보다 낮다면? -> 갈 수 있음
            if 0<=nr < n and 0<= nc <m and arr[nr][nc] < arr[cr][cc]:
                # 방문한 적 있는 애라면?
                if dt[nr][nc]:
                    dt[nr][nc] += dt[cr][cc]
                # 방문한 적 없다면?
                else:
                    dt[nr][nc] = dt[cr][cc]
                    heappush(heap, (-1*arr[nr][nc], nr, nc))



bfs(0, 0)

# 도착점
print(dt[n - 1][m - 1])
