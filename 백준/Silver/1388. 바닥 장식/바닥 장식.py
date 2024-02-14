import sys

input = sys.stdin.readline
length, width = map(int, input().split())

floor = list()
for _ in range(length):
    floor.append(list(input().rstrip()))

visited = [[0] * width for _ in range(length)]


def dfs(graph, row, col):
    visited[row][col] = 1

    if graph[row][col] == '-':
        if col + 1 < width and graph[row][col + 1] == '-' and visited[row][col + 1] == 0:
            dfs(graph, row, col + 1)
    else:
        if row + 1 < length and graph[row + 1][col] == '|' and visited[row + 1][col] == 0:
            dfs(graph, row + 1, col)


cnt = 0
for i in range(length):
    for j in range(width):
        if visited[i][j] == 0:
            cnt += 1
            dfs(floor, i, j)

print(cnt)