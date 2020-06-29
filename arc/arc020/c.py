import sys
input = sys.stdin.readline

n = int(input())
al = [tuple(map(int, input().split())) for _ in range(n)]
b = int(input())

ans = 0
for ai, li in al:
    mi = len(str(ai))
    c = 0
    di = pow(10, mi, b)
    x = pow(10, mi * li, b)
    while li:
        if li % 2 == 1:
            c *= di
            c += ai
            c %= b
        ai = (ai * di + ai) % b
        di = di**2 % b
        li //= 2

    ans = (ans * x + c) % b

print(ans)
