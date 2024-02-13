import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().split())

# 하나 하나 보면서, 맞으면 0으로 바꿔버려도 될듯.

graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))
# print(graph)


# 방문 리스트
visited = [ [0] * m for _ in range(n)]

# '-' 는 오른쪽 dfs , '|'는 아래쪽 dfs
def dfs(r,c):
    visited[r][c]= 1
    if graph[r][c]== '-':
        if c+1 < m and graph[r][c+1] == '-' and visited[r][c+1] == 0:
            dfs(r, c+1)
    elif graph[r][c] =='|':
        if r+1 < n and graph[r+1][c] == '|' and visited[r+1][c] == 0:
            dfs(r+1, c)

# 개수 세기
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            cnt += 1
            dfs(i,j)

print(cnt)

