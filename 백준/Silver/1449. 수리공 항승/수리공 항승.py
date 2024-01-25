# 물이 새는 곳의 개수 N과 테이프 길이 L, 물이 새는 곳의 위치 입력
N, L = map(int, input().split())
L_lst = list(map(int, input().split()))


# 리스트 정렬
L_lst.sort()
start=L_lst[0]
cnt = 1

# 물 새는 곳 하나 하나 막기
for i in L_lst[1:]:
    if i <= start + L-1:
        continue
    else:
        start = i
        cnt +=1

print(cnt)



