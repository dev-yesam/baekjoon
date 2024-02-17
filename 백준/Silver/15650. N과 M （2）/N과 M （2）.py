n, m = map(int, input().split())

# 백트래킹.
res = []
visited = [0] * (n + 1)


def recur(num):
    # 1. 가지치기
    if res != sorted(res):
        return
    # 2. 종료조건
    if num == m:
        print(*res)
        return

    # 3. 재귀호출
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = 1
            res.append(i)
            recur(num + 1)

            # 복구
            res.pop()
            visited[i] = 0

recur(0)
