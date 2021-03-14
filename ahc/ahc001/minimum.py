n = int(input())
xyr = [tuple(map(int, input().split())) for _ in range(n)]

ans = [(xi, yi, xi + 1, yi + 1) for xi, yi, _ in xyr]

for ans_i in ans:
    print(*ans_i)
