# 시작 위치 (1,1)
# 이동 하, 우, 우하 3가지만
# 많은 칸 수 지나가려면?


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# d[i][j] = d[i-1][j] + d[i][j-1]
# 디피 테이블 (패딩 + 1)
d = [[0] * (m + 1) for _ in range(n)]
# 초기값
d[0] = arr[0] + [0]
for i in range(m):
    d[0][i] = d[0][i] + d[0][i - 1]

for i in range(1, n):
    for j in range(m):
        d[i][j] = max(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + arr[i][j]

print(d[n - 1][m - 1])
