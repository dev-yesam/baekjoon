import sys

input = sys.stdin.readline

name_num, power_num = map(int, input().strip().split())
names = [input().strip().split() for _ in range(name_num)]
names = [(x, int(y)) for x, y in names]

# power 마다, names에서 알맞은 거 찾으면 됨.
# power보다 크거나 같으면서 인덱스는 가장 작은거 -1

for _ in range(power_num):
    power = int(input())

    start = 0
    end = name_num - 1
    answer = -1
    while start <= end:

        mid = (start + end) // 2

        if names[mid][1] >= power:
            end = mid - 1
            answer = names[mid][0]

        else:
            start = mid + 1

    print(answer)
