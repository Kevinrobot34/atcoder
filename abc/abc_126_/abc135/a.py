a, b = map(int, input().split())

if abs(a - b) % 2 == 0:
    print(a + (b - a) // 2)
else:
    print("IMPOSSIBLE")
