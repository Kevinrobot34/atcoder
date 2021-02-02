import sys
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

king = 0
ak, bk = ab[king]
for i, (ai, bi) in enumerate(ab):
    if (ak + bi - 1) // bi < (ai + bk - 1) // bk:
        king = i
        ak, bk = ai, bi

is_king = True
for i, (ai, bi) in enumerate(ab):
    if i == king:
        continue
    if (ak + bi - 1) // bi <= (ai + bk - 1) // bk:
        is_king = False
        break

ans = king + 1 if is_king else -1
print(ans)
