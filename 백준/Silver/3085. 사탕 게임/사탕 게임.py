
def count_r(lst):
    cnt = 1
    ans = 1
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 1

    return ans


def count_c(lst,j):
    cnt = 1
    ans = 1
    for i in range(N - 1):
        if lst[i][j] == lst[i + 1][j]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 1

    return ans


# 우측 : 행 열 열
## 전치행렬하면 우측이랑 똑같음. 하측 : 열 행 행

def solve(lst):
    mx = 0
    for i in range(N):
        for j in range(N - 1):
            # 우측과 자리 교환
            lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
            mx = max(mx, count_r(lst[i]),count_c(lst, j),count_c(lst, j+1))
            lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]

    return mx


# 입력값
N = int(input())
arr = [list(input()) for _ in range(N)]

# 전치행렬 만들기 => 신기하네....
arr_t = list(map(list, zip(*arr)))

ans = max(solve(arr), solve(arr_t))
print(ans)

