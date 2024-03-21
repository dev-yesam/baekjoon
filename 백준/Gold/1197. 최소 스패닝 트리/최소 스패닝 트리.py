import heapq


def prim(start):
    visited = [0] * (v+1)
    heap = []
    sum_weight = 0

    # 시작점 처리
    heapq.heappush(heap, (0, start))

    # 방문 예약
    while heap:
        # 꺼내기
        weight, now = heapq.heappop(heap)

        if visited[now]:
            continue

        # 밑에서 미리 방문 처리하면 안되는 구나. 여러 후보군 중에서 결국 최소힙으로 나오는 걸 골라야하니까.
        visited[now] = 1
        sum_weight += weight

        for next_weight, next_node in adjl[now]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_weight, next_node))

    return sum_weight


# 그래프 정보 입력
v, e = map(int, input().split())
adjl = [[] for _ in range(v+1)]
for _ in range(e):
    s, e, w = map(int, input().split())
    adjl[s].append((w, e))
    adjl[e].append((w, s))



# prim 알고리즘
ans = prim(1)
print(ans)
