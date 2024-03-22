from heapq import heappush, heappop


def dijkstra(start):
    # 시작점
    pq = []
    pq.append((0,start))
    dists[start][start]=0


    # 방문예약
    while pq:
        # 꺼내기
        now_dist, now = heappop(pq)

        if now_dist > dists[start][now]:
            continue

        # 다음 방문 예약
        for next_weight, next in adjl[now]:
            next_dist = now_dist + next_weight
            if next_dist < dists[start][next]:
                heappush(pq, (next_dist, next))
                dists[start][next] = next_dist
        

# n 마을 수 m 도로 수, x 목표 마을
n, m, x = map(int, input().split())
adjl = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adjl[s].append((w, e))

# 양방향 다익스트라
INF = 100000
dists = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dijkstra(i)


# 최대 시간
ans = 0
for i in range(1, n + 1):
    if i == x:
        continue
    cnt = dists[i][x] + dists[x][i]
    if ans < cnt:
        ans = cnt


# 가장 오랜 시간이 걸린 학생
print(ans)
