# 큰 괄호에 레이저 개수 + 1개 만큼 잘린 조각 생김

ans = 0
# 여는 괄호 만나면, 그 개수만큼 레이저 만났을 때 조각 생김.
# 여는 괄호 개수 x라고 하면, 레이저 만날 때 마다 +x가 되고, 닫는 괄호 만나면, x-1이 되는 것.
# 닫는 괄호 만나면, 그것도 개수에 +1하면 됨.
stack = []
all_str = []
num_open = 0

loc = input()

for i in loc:
    all_str.append(i)
    if i == "(":
        stack.append(i)
        
    elif i == ')':

        # 레이저냐 아니냐.
        if all_str[-2] == "(":
            stack.pop()
            ans += len(stack)

        else:
            stack.pop()
            ans += 1

print(ans)
# 3 4 4 2 3 1 2 1 1 1 1 1
