import sys

input = sys.stdin.readline

## 신발끈 공식 써야함

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
length = lst[0][1]-lst[0][0]
for i in range(1,n):
    # 겹친다면?
    if lst[i-1][1] >= lst[i][0]:
        # 확장된다면?
        if lst[i-1][1] < lst[i][1]:
            length += lst[i][1]-lst[i-1][1]
        # 확장안되면?
        else:
            lst[i][1] = lst[i-1][1]
    # 안겹치면?
    else:
        length += lst[i][1]-lst[i][0]
print(length)