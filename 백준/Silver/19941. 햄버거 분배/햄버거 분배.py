# 19941 재 재출
import sys

n, k = map(int,sys.stdin.readline().split())
locations = list(sys.stdin.readline().rstrip())
# 우측으로 탐색하며 가장 왼쪽에 있는 햄버거 먹기

#카운트
cnt = 0

# 반복문 돌리며, 탐색
for idx in range(n):
    if locations[idx] == 'P':

        # i위치에서 -k~ k 까지 탐색하며, 가장 왼쪽 햄버거 퍼먹기 
        for i in range(max(idx-k,0), min(idx+k+1, n)):
            if locations[i]=='H':
                locations[i]=0
                cnt+=1
                break

# 출력
print(cnt)