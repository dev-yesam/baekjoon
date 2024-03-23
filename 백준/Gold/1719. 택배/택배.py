from heapq import heappush, heappop


def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    dists[start][start] = 0

    while pq:
        # 꺼내기
        now_dist, now = heappop(pq)

        if now_dist > dists[start][now]:
            continue

        # 다음 노드
        for next_weight, next in adjl[now]:
            next_dist = next_weight + now_dist
            if next_dist < dists[start][next]:
                dists[start][next] = next_dist
                heappush(pq, (next_dist, next))

                # 경로 추가 (이전 경로 + 현재 위치)
                tr[start][next] = tr[start][now] + [next]


# 경로표 => 최단 경로
# 최단 거리가 아닌 최단 경로가 필요. => 경유지 저장해야함.

n, m = map(int, input().split())
adjl = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adjl[s].append((w, e))
    adjl[e].append((w, s))

INF = 200000
dists = [[INF] * (n + 1) for _ in range(n + 1)]
tr = [[[] for _ in range(n + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    dijkstra(i)

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if not tr[i][j]:
            print('-', end=' ')
        else:
            print(tr[i][j][0], end=' ')
    print()
