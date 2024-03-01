def isqueen(i, j):
    # 좌상 대각선
    for diag1 in range(-n + 1, 0):
        if 0 <= i + diag1 < n and 0 <= j + diag1 < n and arr[i + diag1][j + diag1] == 1:
            return False

    # 우상 대각선
    for diag2 in range(-n + 1, 0):
        if 0 <= i + diag2 < n and 0 <= j - diag2 < n and arr[i+diag2][j-diag2] == 1:
            return False

    return True



def recur(level,row):
    global cnt
    # 종료 조건
    if level == n:
        cnt += 1
        return

    # 재귀 호출
    for i in range(n):
        # 방문하지 않았으며, 퀸이 겹치지 않으면
        if not col_visited[i] and isqueen(row,i) :
            col_visited[i] = 1
            arr[row][i] = 1

            recur(level+1, row+1)
            # 복구
            col_visited[i] = 0
            arr[row][i] = 0


n = int(input())
arr = [[0] * n for _ in range(n)]
cnt = 0

col_visited = [0] * n


recur(0,0)

print(cnt)