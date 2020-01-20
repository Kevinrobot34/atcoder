n, y = map(int, input().split())

def solve(n, y):
    for a in range(min(y // 10000, n) + 1):
        for b in range(min(y // 5000, n) + 1):
            if a + b > n or 10000 * a + 5000 * b > y:
                continue

            c = n - a - b
            if 10000 * a + 5000 * b + 1000 * c == y:
                print(a, b, c)
                return

    print("-1 -1 -1")

solve(n, y)
