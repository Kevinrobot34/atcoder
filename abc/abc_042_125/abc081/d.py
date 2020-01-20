n = int(input())
a = list(map(int, input().split()))

a_max = -10**7
a_max_idx = -1
a_min = 10**7
a_max_idx = -1
for i, ai in enumerate(a):
    if a_max < ai:
        a_max = ai
        a_max_idx = i
    if a_min > ai:
        a_min = ai
        a_min_idx = i

operation = []
if abs(a_max) > abs(a_min):
    for i, ai in enumerate(a):
        if ai < 0:
            operation.append((a_max_idx + 1, i + 1))
    # 全てが正になる
    for i in range(1, n):
        operation.append((i, i + 1))
else:
    for i, ai in enumerate(a):
        if ai > 0:
            operation.append((a_min_idx + 1, i + 1))
    # 全てが正になる
    for i in reversed(range(1, n)):
        operation.append((i + 1, i))

print(len(operation))
for opi in operation:
    print(*opi)
