import sys

input = sys.stdin.readline

# V 정점의 수, E 간선의 수, start 시작 정점
V, E, start = map(int, input().rstrip().split())

# 인접리스트
adjl = [[] for _ in range(V + 1)]

# 간선 입력
for edge in range(E):
    a, b = map(int, input().rstrip().split())
    adjl[a].append(b)
    adjl[b].append(a)

# 인접 리스트 정렬
for v in adjl:
    v.sort()

#
visited = [0] * (V + 1)

# dfs 생성
def dfs(graph, V, start):

    stack = []
    now = start
    cnt = 1
    visited[now] = cnt
    while True:

        for vtx in adjl[now]:

            if not visited[vtx]:
                adjl[now].pop(0)
                adjl[vtx].remove(now)
                stack.append(now)

                now = vtx
                cnt += 1
                visited[vtx] = cnt

                break

        else:
            if stack:
                now = stack.pop()
            else:
                break

    return visited


lst = dfs(adjl, V, start)[1:]
for i in lst:
    print(i)