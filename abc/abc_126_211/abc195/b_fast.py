a, b, w = map(int, input().split())
w *= 1000
ans_min = (w + b - 1) // b
ans_max = w // a
if ans_min > ans_max:
    print('UNSATISFIABLE')
else:
    print(ans_min, ans_max)
