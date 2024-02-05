N, M = map(int, input().split())
titles = [tuple(input().split()) for _ in range(N)]
titles = [(title, int(power)) for title, power in titles]

# 전투력에 따라 정렬
titles.sort(key=lambda x: x[1])

powers = [int(input()) for _ in range(M)]

for power in powers:
    # 이진 탐색으로 적절한 칭호 찾기
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if titles[mid][1] < power:
            start = mid + 1
        else:
            end = mid - 1

    # 경계 조건 확인
    if start >= N:
        start = N - 1
    elif start < 0:
        start = 0

    print(titles[start][0])
