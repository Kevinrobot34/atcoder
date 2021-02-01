import sys
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ans = len(set((ai, bi) if ai < bi else (bi, ai) for ai, bi in ab))
print(ans)
