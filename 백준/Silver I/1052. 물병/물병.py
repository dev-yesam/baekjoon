# 입력
bottles, k = map(int, input().split())

# 현재 물병 수 : 2진수로 바꿨을 때, 1의 개수
bi_bottles = bin(bottles)[2:]
now_bottles = bi_bottles.count('1')

if now_bottles <= k:
    print(0)
    exit()

# 13 : 8 4 1 => 1101 => 4- '01'
# 2진법 앞에서 k번째 1에서 남은 애들 빼준만큼 더해주면 되네.

cnt = 0
idx_n = 0
for idx in range(len(bi_bottles)):
    if bi_bottles[idx] == '1':
        cnt += 1
        if cnt == k:
            idx_n = idx

answer = int(bi_bottles[idx_n:], 2) - 2 * int(bi_bottles[idx_n + 1:], 2)

print(answer)
