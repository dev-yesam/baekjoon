n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B 복사하기
C = B[:]

# 정렬하기
A.sort()
C.sort(reverse=True)

# 최솟값 계산
res = 0
for i in range(n):
    res += A[i] * C[i]
    
print(res)