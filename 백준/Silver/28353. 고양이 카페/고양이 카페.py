#28353

# sys 연습. input만 맨날 썼어서 sys도 써봐야 할 듯.
import sys

n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

#카운트
cnt = 0

# 리스트 내림차순
lst.sort(reverse=True)


# 반복문 돌면서 최댓값+최솟값 합쳐서 확인
for idx in range(len(lst)):
    #인덱스가 len(lst)-1보다 크거나 같다면 break
    if idx >=len(lst)-1:
        break
    if lst[idx]+lst[-1] <= k:
        cnt+=1
        lst.pop() #최솟값 제거
        
        
        

# 출력
print(cnt)

