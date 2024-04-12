def dfs(r, c, direction, cnt):
    global ans
    if cnt >= 5:
        ans = True
        return
    # 우측
    if direction == 'hor':
        hor_visited[r][c] = 1
        if c + 1 < n and arr[r][c+1]=='o':
            dfs(r, c + 1, 'hor', cnt + 1)
    # 하측
    elif direction == 'ver':
        ver_visited[r][c] = 1
        if r + 1 < n and arr[r+1][c]=='o':
            dfs(r + 1, c, 'ver', cnt + 1)

    # 좌하 대각선
    elif direction == 'adiag':
        adiag_visited[r][c] = 1
        if r + 1 < n and c - 1 >= 0 and arr[r+1][c-1]=='o':
            dfs(r + 1, c - 1, 'adiag', cnt + 1)

    # 우하 대각선
    else:
        ddiag_visited[r][c] = 1
        if r + 1 < n and c + 1 < n and arr[r+1][c+1]=='o':
            dfs(r + 1, c + 1, 'ddiag', cnt + 1)


def solve():
    global ans
    # 우측, 하측, 우하, 좌하만 확인하면 됨.

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                if not hor_visited[i][j]:
                    dfs(i, j, 'hor', 1)
                if not ver_visited[i][j]:
                    dfs(i, j, 'ver', 1)
                if not adiag_visited[i][j]:
                    dfs(i, j, 'adiag', 1)
                if not ddiag_visited[i][j]:
                    dfs(i, j, 'ddiag', 1)

                if ans == True:
                    return True


##########################################################

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [input() for _ in range(n)]

    hor_visited = [[0] * n for _ in range(n)]
    ver_visited = [[0] * n for _ in range(n)]
    adiag_visited = [[0] * n for _ in range(n)]
    ddiag_visited = [[0] * n for _ in range(n)]

    ########
    ans = False
    temp = solve()
    if temp:
        result = 'YES'
    else:
        result = 'NO'

    print(f"#{tc}", result)
