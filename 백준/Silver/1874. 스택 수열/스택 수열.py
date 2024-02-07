n= int(input())

stack = []
answer = []
found = True

now = 1
for _ in range(n):

    num = int(input())

    while now <= num:
        answer.append("+")
        stack.append(now)
        now += 1

    if stack[-1] == num:
        answer.append("-")
        stack.pop()

    elif stack[-1] != num:
        found =False

if not found:
    print("NO")

else:
    for i in answer:
        print(i)
