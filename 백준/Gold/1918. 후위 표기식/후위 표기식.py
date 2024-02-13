s = input()

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

stack = []
ans = ''

for tk in s:

    if not stack and tk in icp:
        stack.append(tk)

    elif stack and tk in icp:
        if isp[stack[-1]] < icp[tk]:
            stack.append(tk)
        else:
            while stack and isp[stack[-1]] >= icp[tk]:
                ans += stack.pop()
            stack.append(tk)

    elif tk == ')':
        while stack[-1] != '(':
            ans += stack.pop()
        stack.pop()

    else:
        ans += tk

while stack:
    ans += stack.pop()

print(ans)
# print(stack)