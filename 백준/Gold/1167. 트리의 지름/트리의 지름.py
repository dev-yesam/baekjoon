import sys
sys.setrecursionlimit(10**5)


# 입력값
v = int(input())

# 트리 정보 인접 리스트
adjl = [[] for _ in range(v + 1)]

# 트리 정보 입력
for _ in range(v):
    lst = list(map(int, input().split()))
    node = lst.pop(0)
    while True:
        if lst[0] == -1:
            break
        else:
            c = lst.pop(0)
            distance = lst.pop(0)
            adjl[node].append((c, distance))
            # adjl[c].append((node, distance))

# 트리의 지름
mx = 0
# mx_node = 0

def dfs(start, weight):
    global mx, mx_node
    visited[start]= 1


    # 거리가 크냐
    if mx < weight:
        mx = weight
        mx_node = start

    # dfs 
    for i in adjl[start]:
        if not visited[i[0]]:
            dfs(i[0], weight + i[1])


visited = [0] * (v + 1)
dfs(1, 0)

visited = [0] * (v + 1)
dfs(mx_node, 0)

print(mx)