import sys
input = sys.stdin.readline


def find_set(x):
    if x == p[x]:
        return x

    else:
        p[x] = find_set(p[x])
        return p[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        p[y] = x
    else:
        p[x] = y


def kruskal():
    ans = 0
    cnt = 0
    for s, e, w in edges:
        if find_set(s) != find_set(e):
            union(s, e)
            ans += w
            cnt += 1
            if cnt == n - 2:
                return ans
    return 0

n, m = map(int, input().split())
edges = []
p = [i for i in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))
    # mst 만든 다음에 제일 가중치 높은 간선 없애면 되겠네.

edges.sort(key=lambda x: x[2])

# 크루스칼 써야할 듯.
ans = kruskal()

print(ans)
