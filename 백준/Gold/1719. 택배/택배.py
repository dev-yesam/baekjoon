from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def dijkstra(start):
    # 시작점
    tr[start][start] = '-'
    dists = [INF] * (n + 1)
    dists[start] =0
    pq = []
    heappush(pq, (0, start))

    # 다음 방문 예약
    while pq:
        # 꺼내기
        dist, now = heappop(pq)

        # 꺼냈는데 전보다 작다?
        if dists[now] < dist:
            continue

        # 다음 방문
        for next_weight, next in adjl[now]:
            next_dist = dist + next_weight
            if next_dist < dists[next]:
                dists[next] = next_dist
                heappush(pq, (next_dist, next))

                # 시작점에서 바로 갔다면?
                if now == start:
                    tr[start][next] = next
                # now가 경유지라면?(그래서 뭐가 now에 들어있다면?)
                elif tr[start][now]:
                    tr[start][next] = tr[start][now]




n, m = map(int, input().split())  # 노드의 수, 간선의 수
adjl = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adjl[a].append((w, b))
    adjl[b].append((w, a))

tr = [[0] * (n + 1) for _ in range(n + 1)]  # 경로표

# 다익스트라 호출
INF = 3000000
for i in range(1, n + 1):
    dijkstra(i)

# 출력
for i in range(1, n + 1):
    print(*tr[i][1:])
