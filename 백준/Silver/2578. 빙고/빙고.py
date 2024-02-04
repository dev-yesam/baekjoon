arr = [list(map(int, input().split())) for _ in range(5)]

lst = []
for i in range(5):
    lst.extend(list(map(int, input().split())))

cnt = 0
for num in lst:
    cnt += 1
    # 찾고 지우고,
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                arr[i][j] = 0

    # 빙고 확인하고.
    bingo = 0

    # 가로 빙고 확인
    for i in range(5):
        if all(arr[i][j] == 0 for j in range(5)):
            bingo += 1

    # 세로 빙고 확인
    for j in range(5):
        if all(arr[i][j] == 0 for i in range(5)):
            bingo += 1

    # 대각 빙고 확인
    if all(arr[i][i] == 0 for i in range(5)):
        bingo += 1

    if all(arr[i][5 - i - 1] == 0 for i in range(5)):
        bingo += 1

    if bingo >= 3:
        print(cnt)
        break
