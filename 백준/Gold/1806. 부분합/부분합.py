# n 수열의 길이, 합이 s 이상.
n, s = map(int, input().split())
lst = list(map(int, input().split()))

# 길이는 작을수록, 합은 s이상이어야함. 불가능하면 0출력

ans = n + 1  # 최종 길이
start, end = 0, 0
total = lst[0]  # 구간 합

while True:
    length = end + 1 - start

    # s 보다 작다면
    if total < s:
        end += 1

        # 범위를 넘는다면?
        if end >= n:
            break
        # 범위 내라면
        else:
            total += lst[end]

    # s 보다 크거나 같다면
    else:
        if length < ans:  # 갱신
            ans = length
        
        total -= lst[start]
        start += 1
  
        # 범위를 넘는다?
        if start >= n:
            break
        

# 출력
if ans > n:
    print(0)
else:
    print(ans)
