import sys
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ans = sum(min(ai // 2, bi) for ai, bi in ab)
print(ans)
