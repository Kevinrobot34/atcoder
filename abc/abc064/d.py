from collections import deque
n = int(input())
s = input()

stack = deque()
for i in range(n):
    if len(stack) > 0:
        stack_last = stack.pop()
        if stack_last == "(" and s[i] == ")":
            continue
        else:
            stack.append(stack_last)
            stack.append(s[i])
    else:
        stack.append(s[i])

# print(stack)
for i in range(len(stack)):
    if stack[i] == '(':
        s = s + ')'
    else:
        s = '(' + s

print(s)
