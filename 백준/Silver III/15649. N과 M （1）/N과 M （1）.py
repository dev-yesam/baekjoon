n, m = map(int, input().split())
b = []


def bt(start, end, lst):
    if start > end:
        print(*lst)
        return

    for i in range(1,n+1):
        if i not in lst:
            lst.append(i)
            bt(start + 1,end, lst)
            lst.pop()

bt(1,m,b)