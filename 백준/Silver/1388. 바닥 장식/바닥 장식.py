# n 세로 길이, m 가로 길이
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

visited = [[0] *m for _ in range(n)]


def dfs(r,c):

    visited[r][c] = 1

    if graph[r][c] == '-':
        if c+1 < m and graph[r][c+1] == '-' and visited[r][c+1] ==0:
            dfs(r,c+1)
    elif graph[r][c] == '|':
        if r+1 < n and graph[r+1][c] == '|' and visited[r+1][c] == 0:
            dfs(r+1,c)

# 개수 세기
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            cnt += 1
            dfs(i, j)

print(cnt)