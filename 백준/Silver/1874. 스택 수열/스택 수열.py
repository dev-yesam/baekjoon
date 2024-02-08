import sys
input = sys.stdin.readline

n = int(input())
stack =[0]
lst = []


num = 1
answer = True
for _ in range(n):
    x = int(input())
    # 가능하면 +, - 로 출력



    while num < x:
        # x 보다 작을 때
        stack.append(num)
        lst.append('+')
        num += 1


    # x 와 같을 때
    if num == x:
        lst.append('+')
        lst.append('-')
        num +=1

    # x 보다 클 때
    elif num > x:
        if stack[-1] == x:
            lst.append('-')
            stack.pop()
        else:
            answer = False
            break

if answer:
    for i in lst:
        print(i)
else:
    print("NO")
