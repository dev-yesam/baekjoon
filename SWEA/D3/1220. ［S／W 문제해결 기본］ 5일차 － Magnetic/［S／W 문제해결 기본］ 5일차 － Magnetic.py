# 위에서부터 빨간색을 만나면 prev에 넣고.
# prev 밑으로 내려가면서 파란색 만나면 cnt += 1

t = 10
for tc in range(1, 11):
    n = int(input())  # 어차피 100
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for j in range(100):
        prev = 0
        for i in range(100):
            if arr[i][j] == 1:
                prev = 1
            elif arr[i][j] == 2 and prev == 1:
                cnt += 1
                prev = 2

    print(f'#{tc}', cnt)
