import sys
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ans = [abs(ai - bi) if ai != bi else -1 for ai, bi in ab]
print(*ans, sep='\n')
