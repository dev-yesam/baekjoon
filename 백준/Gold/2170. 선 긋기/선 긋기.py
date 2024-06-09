import sys

input = sys.stdin.readline



n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
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
            new_tuple = (lst[i][0], lst[i-1][1])
            lst[i] = new_tuple

    # 안겹치면?
    else:
        length += lst[i][1]-lst[i][0]
print(length)