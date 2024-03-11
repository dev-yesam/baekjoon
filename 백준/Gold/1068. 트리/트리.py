# 입력
from collections import deque

n = int(input())

# 자식 인덱스로 부모 저장
arr = list(map(int, input().split()))

# 지울 번호 리스트
x = int(input())
lst = []
lst.append(x)

# 지운 번호는 -2 두자
arr[x] = -2
for i in range(x + 1, n):
    if arr[i] in lst:
        lst.append(i)
        arr[i] = -2


# 부모 인덱스로 자식 저장
tree= [[] for _ in range(n)]
for i in range(n):
    if arr[i] == -2:
        pass
    elif arr[i] == -1:
        root = i
    else:
        tree[arr[i]].append(i)

cnt =0
visited = [0] *n
def dfs(root):
    global cnt
    visited[root] =1
    # 1. 종료조건
    if not tree[root]:
        cnt +=1
        return
    # 2. 가지치기

    # 3. 재귀호출
    for i in tree[root]:
        if not visited[i] and arr[i] != -2:
            dfs(i)

if -1 in arr:
    dfs(root)
    print(cnt)
else:
    print(0)










# # 자식있는 번호 리스트
# lst2= []
# cnt = 0
# for i in range(n):
#     # 부모가 있다면
#     if arr[i] != -2:
#         if i not in lst2:
#             lst.append(arr[i])
#             lst.append(i)
#             cnt += 1
#         else:
#             lst2.append(arr[i])
