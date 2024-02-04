# 거북이

# 움직임
moves = {"F": 1, "B": -1}
rotations = {"L": -1, "R": 1}

# 우회전 기준 : 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0


# 입력
t = int(input())
for _ in range(t):

    # 현 위치
    x, y = 0, 0

    Mx, mx, My, my = 0, 0, 0, 0

    directions = input()

    for direction in directions:
        if direction in moves:
            x += dx[d] * moves[direction]
            y += dy[d] * moves[direction]

        elif direction in rotations:
            d = (d + rotations[direction]) % 4

        Mx, My = max(Mx, x), max(My, y)
        mx, my = min(mx, x), min(my, y)

    area = (Mx - mx) * (My - my)
    print(area)
