t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    ans_bin = 0
    cnt = 1
    x =((1 << 10) - 1)
    while True:
        cmp_bin = str(n * cnt)
        for b in cmp_bin:
            ans_bin = ans_bin | (1 << int(b))

        if ans_bin & x ==x:
            break
        cnt += 1

    print(f'#{tc}', cmp_bin)
