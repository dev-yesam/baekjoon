n = int(input())

#
# n자리 일 때 개수 = d[n]

d = [[0] * 10 for _ in range(n + 1)]

d[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    for j in range(10):
        d[i][j] = sum(d[i-1][j:])

ans = sum(d[n])
print(ans % 10007)
