import sys
input = sys.stdin.readline

stack = []

n = int(input())
for i in range(n):
    dir = list(map(int, input().split()))

    if dir[0] == 1:
        stack.append(dir[1])

    elif dir[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif dir[0] == 3:
        print(len(stack))

    elif dir[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)