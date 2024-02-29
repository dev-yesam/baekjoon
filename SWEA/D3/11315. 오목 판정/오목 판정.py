def omok(r, c):
    dr = [1, 0, 1, 1]  # |하, -우, \우하, /좌하
    dc = [0, 1, 1, -1]  # |하, -우, \우하, /좌하

    # 4방향 탐색
    for d in range(4):
        # 기준 좌표에 돌이 있음
        cnt = 1
        # 돌 4개를 탐색
        for power in range(1, 5):
            nr = r + (dr[d] * power)
            nc = c + (dc[d] * power)
            if not (0 <= nr < n and 0 <= nc < n):
                break

            # 돌을 발견하면 cnt
            if arr[nr][nc] == 'o':
                cnt += 1

            # 오목이면
            if cnt == 5:
                return True

    return False


def game_start():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                if omok(i, j):
                    return "YES"
    return "NO"


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    ans = game_start()
    print(f'#{tc}', ans)
