# 11497

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().rstrip().split()))

    # 내림차순 정렬
    lst.sort(reverse=True)

    # 돌면서 넣기
    res = 0
    new_lst=[lst[0]]
    for i in range(1,len(lst)):
        if i%2 ==1:
            new_lst.insert(0,lst[i])
            if res < new_lst[1]-new_lst[0]:
                res = new_lst[1]-new_lst[0]

        else:
            new_lst.append(lst[i])
            if res < new_lst[-2]-new_lst[-1]:
                res =new_lst[-2]-new_lst[-1]
    
    if res < abs(new_lst[0]-new_lst[-1]):
        res=abs(new_lst[0]-new_lst[-1])
    
    print(res)

