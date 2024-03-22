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


import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

p = [i for i in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 1:
            union(i, j)

travels = list(map(int, input().split()))
prev = find_set(travels[0]-1)
ans = "YES"
for i in range(1, len(travels)):
    if prev != find_set(travels[i]-1):
        ans = "NO"
        break

print(ans)
