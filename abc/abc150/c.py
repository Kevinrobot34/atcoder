from itertools import permutations
n = int(input())
p = list(map(lambda x: int(x) - 1, input().split()))
q = list(map(lambda x: int(x) - 1, input().split()))


def compare(a, b):
    for i in range(n):
        if a[i] != b[i]:
            return False
    return True


idx_p = -1
idx_q = -1
for i, x in enumerate(permutations(range(n))):
    if compare(p, x):
        idx_p = i
    if compare(q, x):
        idx_q = i

ans = abs(idx_p - idx_q)
print(ans)
