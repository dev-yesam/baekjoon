# 좌상 대각선과 우상 대각선 확인 해야함.
def diag(r, c):
    # 좌상 대각선 => r-x,c-x -> x: 0~ n-1  & 범위 이탈 여부 확인
    for x in range(1, n):
        if 0 <= r - x and c - x >= 0 and arr[r - x][c - x] == 1:
            return False
    # 우상 대각선 => r-x,c+x -> x: 0~ n-1 & 범위 이탈 여부 확인
    for x in range(1, n):
        if 0 <= r - x and c + x < n and arr[r - x][c + x] == 1:
            return False

    # 그외
    return True

# back-tracking function
def recur(level):
    global cnt
    if level == n: #  full-placed
        cnt += 1
        return

    # place the queen
    for col in range(n):
        # can place?
        if not col_visited[col] and diag(level,col):
            col_visited[col] = 1
            arr[level][col] = 1
            recur(level+1)
            col_visited[col] = 0
            arr[level][col] = 0

n = int(input())
arr = [ [0]*n for _ in range(n)]

# 각 row 마다 위에서부터 하나씩 놓으면 됨
# 각 col 마다 겹치면 안됨 -> col_lst = []
col_visited = [0] * n

# count
cnt =0

# call the function
recur(0)

# print
print(cnt)