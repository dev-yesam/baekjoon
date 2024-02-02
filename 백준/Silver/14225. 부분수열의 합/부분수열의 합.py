import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

lst_sum = 0
for i in lst:
    if i > lst_sum + 1:
        print(lst_sum + 1)
        break
    else:
        lst_sum += i

else:
    print(lst_sum + 1)
