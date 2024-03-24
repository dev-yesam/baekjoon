from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
    # 시작점
    dists[start][start] = 0
    pq = []
    heappush(pq, (0,start))

    while pq:
        #꺼내기
        dist, now = heappop(pq)

        if dist > dists[start][now]:
            continue

        for next_weight, next in adjl[now]:
            next_dist = next_weight + dists[start][now]
            if next_dist < dists[start][next]:
                dists[start][next] = next_dist
                heappush(pq, (next_dist, next))


# n 마을의 수 , m 간선의 수, x 목적지
n, m, x = map(int, input().split())
adjl = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adjl[a].append((w, b))
    adjl[a].append((w, a))

# 거리 2차원 배열
INF = 200000
dists = [[INF] * (n + 1) for _ in range(n + 1)]

# 다익스트라 2차원
for i in range(1,n+1):
    dijkstra(i)

# 최대 시간
maxv = 0
for i in range(1,n+1):
    maxv = max(maxv, dists[i][x]+dists[x][i])

print(maxv)