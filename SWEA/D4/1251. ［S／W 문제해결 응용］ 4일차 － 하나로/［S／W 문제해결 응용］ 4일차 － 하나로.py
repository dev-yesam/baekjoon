from heapq import heappush, heappop


# 최소 신장 트리 문제
# 간선 수가 많을 수 있으니 프림

def prim(start):
    visited = [0] * n
    heap = []
    heappush(heap, (0, start))
    total = 0
    cnt = 0
    # 방문 예약
    while heap:
        weight, now = heappop(heap)

        # 이미 방문한 적 있다면
        if visited[now]:
            continue

        visited[now] = 1
        total += weight

        cnt += 1
        if cnt == n: break  # 최적화

        for next in range(n):
            if not visited[next]:
                dist = (x_lst[now] - x_lst[next]) ** 2 + (y_lst[now] - y_lst[next]) ** 2
                heappush(heap, (dist*e, next))

    return total


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    e = float(input())

    # 최소 환경 부담금
    ans = prim(0)

    print(f'#{tc}', round(ans))
