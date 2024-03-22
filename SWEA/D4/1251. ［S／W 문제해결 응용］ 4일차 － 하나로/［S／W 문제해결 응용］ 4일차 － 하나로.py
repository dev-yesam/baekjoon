from heapq import heappush, heappop


# 프림 함수 (bfs 응용)
def prim(start):
    visited = [0] * n
    heap = []
    sum_weight = 0
    cnt = 0
    # 시작점
    # visited[start] = 1 => 밑에서 처리하기에 생략 가능
    heappush(heap, (0, 0))  # 가중치, 해당 노드

    # 방문 예약
    while heap:
        # 꺼내기
        now_weight, now_node = heappop(heap)

        # 이미 방문했냐
        if visited[now_node]:
            continue

        visited[now_node] = 1
        sum_weight += now_weight



        # 다음 노드
        for next in range(n):
            if not visited[next]:
                dist = (x_lst[now_node] - x_lst[next]) ** 2 + (y_lst[now_node] - y_lst[next]) ** 2
                price = e * dist
                heappush(heap, (price, next))

    return round(sum_weight)


t = int(input())
for tc in range(1, t + 1):
    # 섬의 개수
    n = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    # 세율
    e = float(input())

    # 비용 = 세율 * 길이^2
    # 간선이 어마 어마 하게 많음 => 프림 사용

    ans = prim(0)

    # 출력
    print(f'#{tc}', ans)
