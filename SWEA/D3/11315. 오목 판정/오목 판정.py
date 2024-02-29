def f(r, c):
    # 우 하 우하 좌하 - | \ /  탐색
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    for d in range(4):
        cnt = 1
        # 거리 차이
        for m in range(1, 5):

            nr = r + dr[d]*m
            nc = c + dc[d]*m
            # 범위를 벗어난다면
            if not (0 <= nr < n and 0 <= nc < n):
                break
            # 돌이 있다면 카운트 증가
            if arr[nr][nc] == 'o':
                cnt += 1
            # 오목이면 True 반환
            if cnt == 5:
                return True

    return False

def game():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                if f(i, j):
                    return 'YES'
    return "NO"

t = int(input())
for tc in range(1, t + 1):

    n = int(input())
    arr = [list(input()) for _ in range(n)]

    ans = game()

    print(f'#{tc}', ans)