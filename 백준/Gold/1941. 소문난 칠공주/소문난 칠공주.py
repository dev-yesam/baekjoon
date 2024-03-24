from collections import deque


def bfs(x, y, cmb):
    visited = [[0] * 5 for _ in range(5)]
    # 시작점 처리
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    cnt = 1  # 7공주 수 세기

    # 다음 방문 예약
    while q:
        cx, cy = q.popleft()

        for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and cmb[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
                if cnt == 7:
                    return True

    # 연결 안 돼 있으면
    return False


def recur(level, start):
    global ans
    if level == 7:
        cmb = [[0] * 5 for _ in range(5)]
        s_num = 0
        for c in temp:
            cmb[c // 5][c % 5] = 1
            if arr[c//5][c%5] == "S":
                s_num += 1
        if s_num <4:
            return
        if bfs(temp[0] // 5, temp[0] % 5, cmb):
            ans += 1
            return

    for i in range(start, 25):
        temp.append(i)
        recur(level + 1, i + 1)
        temp.pop()


arr = [list(input()) for _ in range(5)]
ans = 0  # 경우의 수
# 1) 25개 중 7 개를 고르는 조합
# 2) 그 7개가 서로 연결 돼 있는지 판단하는 bfs


# 1) 7 개 고르는 조합 => 백트래킹으로
temp = []
recur(0, 0)
print(ans)
