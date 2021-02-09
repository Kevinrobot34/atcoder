import sys
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0] + x[1], reverse=True)

ans = sum(ai + bi for ai, bi in ab[::2]) - sum(bi for _, bi in ab)
print(ans)
