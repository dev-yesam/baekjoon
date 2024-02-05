# 입력

kids_num, snacks_num = map(int, input().split())
snacks = list(map(int, input().split()))

start = 1
end = max(snacks)

res = 0  # 기본값

while start <= end:
    # 자른 막대과자
    cut_snacks = 0

    # 자르는 지점 middle
    cut = (start + end) // 2

    for snack in snacks:
        cut_snacks += (snack // cut)

    if cut_snacks >= kids_num:
        start = cut +1
        res = cut

    else:
        end = cut - 1

print(res)
