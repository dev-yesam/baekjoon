t = int(input())

for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    max_day = stocks[-1]
    ans = 0
    for i in range(n - 2, -1, -1):
        if stocks[i] > max_day:
            max_day = stocks[i]
        else:
            ans += max_day - stocks[i]

    print(ans)
