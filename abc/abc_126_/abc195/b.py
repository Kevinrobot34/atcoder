a, b, w = map(int, input().split())
w *= 1000

ans_min = w + 1
ans_max = 0
for x in range(1, (w + a - 1) // a + 1):
    if a * x <= w <= b * x:
        ans_min = min(x, ans_min)
        ans_max = max(x, ans_max)

if ans_max == 0 and ans_min == w + 1:
    print('UNSATISFIABLE')
else:
    print(ans_min, ans_max)
