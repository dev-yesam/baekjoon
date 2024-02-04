# 2512

# 입력
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
budget = int(input())

# 모두 배정 가능
if sum(lst) <= budget:
    cutline = max(lst)

# 모두 배정 불가
else:
    # 이진 탐색
    start = 0
    end = max(lst)

    while start <= end:

        mid = (start + end) //2

        # 배정 예산
        sum_lst=0

        for i in lst:
            if i <= mid:
                sum_lst += i
            else:
                sum_lst += mid

        if sum_lst  <= budget:
            cutline = mid
            start = mid+1
        else:
            end = mid-1



print(cutline)