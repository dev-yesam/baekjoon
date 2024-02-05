# X : 현재 게임 횟수
# Y : 이긴 횟수
X, Y = map(int, input().split())
Z = int((Y*100 / X))

start = 0
end = 1e9
res = -1
while start <= end:
    games = (start + end) // 2
    new_Z = ((games + Y)*100) / (games + X)
    if int(new_Z) > Z:
        end = games - 1
        res = games

    else:
        start = games + 1

print(int(res))
