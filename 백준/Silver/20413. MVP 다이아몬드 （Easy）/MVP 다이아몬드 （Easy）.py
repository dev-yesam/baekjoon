# 백준 0128


# 입력
n = int(input())
# 브론즈 -> 다이아 등급 기준액 입력
stdmoney = list(map(int, input().split()))
# MVP 등급 및 최대금액을 담을 리스트
rank = input()
moneylist = [0] #처음에는 최근 1개월 금액이 없으니 0원을 넣어줌

# 3개월
# 30 60 90 150
# B S G

# 랭크 순회하며 최대 금액 탐색
for i in rank:
    mx = 0 #최대 금액
    if i == 'B':
        mx = max(stdmoney[0] - moneylist[-1] -1, 0)
        moneylist.append(mx)
    elif i == 'S':
        mx = max(stdmoney[1] - moneylist[-1] -1, 0)
        moneylist.append(mx)
    elif i == 'G':
        mx = max(stdmoney[2] - moneylist[-1] -1, 0)
        moneylist.append(mx)
    elif i == 'P':
        mx = max(stdmoney[3] - moneylist[-1] -1, 0)
        moneylist.append(mx)
    else: #다이아일 때는 그냥 다이아 기준액만큼이 최대값임
        mx = stdmoney[3]
        moneylist.append(mx)

# 출력
print(sum(moneylist))

        

