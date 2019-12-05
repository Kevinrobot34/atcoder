n = int(input())
ng_list = [int(input()) for _ in range(3)]

if n not in ng_list:
    for i in range(100):
        for j in reversed(range(1, 4)):
            if n - j not in ng_list:
                n -= j
                break

ans = "YES" if n <= 0 else "NO"
print(ans)
