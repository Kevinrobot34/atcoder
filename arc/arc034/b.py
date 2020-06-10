n = int(input())


def func(x):
    return x + sum(map(int, list(str(x))))


ans = []
m = max(1, n - 180)
for x in range(m, n):
    if func(x) == n:
        ans.append(x)
ans.sort()

print(len(ans))
if len(ans) > 0:
    print(*ans, sep='\n')
