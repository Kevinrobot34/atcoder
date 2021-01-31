n = int(input())
a = list(map(int, input().split()))

stack = []
l = [0] * n
for i in range(n):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    l[i] = 0 if len(stack) == 0 else stack[-1] + 1
    stack.append(i)

stack = []
r = [0] * n
for i in reversed(range(n)):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    r[i] = n if len(stack) == 0 else stack[-1]
    stack.append(i)

ans = max(a[i] * (r[i] - l[i]) for i in range(n))
print(ans)
