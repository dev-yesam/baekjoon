# 8911

# 입력
t = int(input())
for tc in range(t):
    s = input()

    # 델타 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 이동과 방향
    move = {'F': 1, 'B': -1}
    directions = {"L": -1, "R": 1}

    # 최대 좌표
    M_x, m_x = 0, 0
    M_y, m_y = 0, 0

    # 방향
    d = 0  # 기본값 상

    # 위치
    r, c = 0, 0

    # 이동
    for i in s:
        if i in move:
            r = r + dr[d] * move[i]
            c = c + dc[d] * move[i]

        elif i in directions:
            d = (d + directions[i]) % 4

        # 최대 최소 좌표 확인
        M_x, m_x = max(M_x, r), min(m_x,r)
        M_y, m_y = max(M_y, c), min(m_y,c)
    
    # 최대 직사각형 넓이 계산 및 출력
    area = (M_x - m_x) * (M_y - m_y)
    print(area)
