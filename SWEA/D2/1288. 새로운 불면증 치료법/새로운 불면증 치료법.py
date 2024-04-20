# 진짜 운이 나빠도 100번까지 곱하면 0~9가 다 나온다고 보장할 수 있음.

t = int(input())
for tc in range(1,t+1):
    n_start = int(input())
    n_nums = 0
    cp = (1<<10)-1
    cnt = 1
    n = str(n_start*cnt)
    while True:
        for num in n:
            n_nums = n_nums | (1<< int(num))

        if n_nums == cp:
            break

        cnt += 1
        n = str(n_start*cnt)

    print(f'#{tc}', n)