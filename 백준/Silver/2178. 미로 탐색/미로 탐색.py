from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

depth = [[0] * m for _ in range(n)]

# 델타 상하 좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# bfs 정의
def bfs(s1, s2):
    # 시작 방문 처리
    depth[s1][s2] = 1
    q = deque()
    q.append((s1, s2))

    # 방문 예약 처리
    while q:
        # 꺼내기
        r, c = q.popleft()

        # 방문 예약
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 방문 범위 인지 가능하냐
            # 방문 처리 및 큐 담기
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == '1' and depth[nr][nc] == 0 :
                depth[nr][nc] = depth[r][c] + 1
                q.append((nr,nc))


bfs(0, 0)
print(depth[n-1][m-1])