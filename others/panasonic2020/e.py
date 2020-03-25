a = input()
b = input()
c = input()

OFFSETS = 9000


def comp(x, y):
    return (x == '?') or (y == '?') or (x == y)


def check(s, t):
    check_st = [True] * (OFFSETS * 2 + 10)
    for i, si in enumerate(s):
        for j, tj in enumerate(t):
            if not comp(si, tj):
                check_st[i - j + OFFSETS] = False
    return check_st


ans = len(a) + len(b) + len(c)
check_ab = check(a, b)
check_bc = check(b, c)
check_ac = check(a, c)
# print(check_ab)
# print(check_bc)
# print(check_ca)

for b_idx in range(-len(b) - len(c), len(a) + len(c) + 1):
    for c_idx in range(-len(b) - len(c), len(a) + len(b) + 1):
        if check_ab[b_idx + OFFSETS] and check_ac[
                c_idx + OFFSETS] and check_bc[c_idx - b_idx + OFFSETS]:
            l_idx = min(0, b_idx, c_idx)
            r_idx = max(len(a), b_idx + len(b), c_idx + len(c))
            ans = min(ans, r_idx - l_idx)

print(ans)
