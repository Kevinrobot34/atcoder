from math import gcd
import sys
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ans = [gcd(ai, bi) for ai, bi in ab]
print(*ans, sep='\n')
