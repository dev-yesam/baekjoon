t = int(input())
for tc in range(1, t + 1):
    rooms = [0] * 401
    n = int(input())
    for _ in range(n):
        s, e = map(int, input().split())

        if s % 2 == 0: s -= 1
        if e % 2 == 0: e -= 1
        if s > e:
            s, e = e, s

        for room in range(s, e + 1):
            rooms[room] += 1

    print(f'#{tc}', max(rooms))
    # print(rooms)

