import sys
sys.setrecursionlimit(10**5)
n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]

# 완전 탐색 하면 되는 거같은데.
visited = [[0] * n for _ in range(n)]

answer = False


def dfs(map, r, c):
    # 현재 위치 바꿀 필요 없음.
    # visited[r][c]= 1

    #
    global answer
    # if answer_right or answer_down :
    if map[r][c] == -1:
        answer = True
        return
    
    if map[r][c] == 0:
        return

    # 이동량
    m = map[r][c]
    # 우측 이동
    if r + m < n:
        dfs(map, r + m, c)
    # 하측 이동
    if c + m < n:
        dfs(map, r, c + m)




dfs(map, 0, 0)
if answer:
    print('HaruHaru')
else:
    print('Hing')
