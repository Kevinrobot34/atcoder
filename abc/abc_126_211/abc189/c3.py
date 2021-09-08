n = int(input())
a = list(map(int, input().split())) + [0]

stack = [(a[0], 0)]  # [(height, left)]
ans = 0
for i in range(1, n + 1):
    if stack[-1][0] < a[i]:
        stack.append((a[i], i))
    elif stack[-1][0] > a[i]:
        while stack and stack[-1][0] >= a[i]:
            h, l = stack.pop()
            ans = max(ans, h * (i - l))
        stack.append((a[i], l))
print(ans)
