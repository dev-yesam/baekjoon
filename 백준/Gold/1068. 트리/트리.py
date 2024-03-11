### 자식 인덱스를 기준으로 부모 노드 정보 저장하는 arr 에서
## 리프노드를 확인하는 방법 익혀두기


n = int(input())

# 자식 인덱스로 부모 저장
arr = list(map(int, input().split()))

# 지울 번호
x = int(input())

# dfs로 삭제
# 지운 번호는 -2 두자
def dfs(x):
    arr[x] = -2
    for i in range(n):
        if arr[i] ==x:
            dfs(i)
dfs(x)

# 카운트
cnt =0

### 리프노드는 이렇게 하면 되겠다.
## 근데 시간이 빠른지는 나중에 생각하면 될듯.
# 리프 노드 확인
for i in range(n):
    # 삭제되지 않았으면서, 누군가의 부모가 아니다.
    if arr[i] != -2 and i not in arr:
        cnt += 1

# 출력
print(cnt)


