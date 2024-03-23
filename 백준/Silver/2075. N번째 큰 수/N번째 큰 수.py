from heapq import heappush, heappop

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# n번째 큰 수는
nums = []
for i in range(n):
    for j in range(n):
        heappush(nums, arr[i][j])

        if len(nums) > n:
            heappop(nums)


print(heappop(nums))

