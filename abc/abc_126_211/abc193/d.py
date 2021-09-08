k = int(input())
s = input()
t = input()


def point(l, c):
    ret = sum(i * pow(10, li + int(i == c)) for i, li in enumerate(l))
    return ret


s_cnt = [0] * 10
t_cnt = [0] * 10
u_cnt = [k] * 10
for si in s[:4]:
    s_cnt[int(si)] += 1
    u_cnt[int(si)] -= 1
for ti in t[:4]:
    t_cnt[int(ti)] += 1
    u_cnt[int(ti)] -= 1

total_cnt = 0
win_cnt = 0
for sp in range(1, 10):
    for tp in range(1, 10):
        if sp == tp:
            if u_cnt[sp] < 2:
                continue
            x = u_cnt[sp] * (u_cnt[sp] - 1)
        else:
            if u_cnt[sp] == 0 and u_cnt[tp] == 0:
                continue
            x = u_cnt[sp] * u_cnt[tp]

        total_cnt += x
        if point(s_cnt, sp) > point(t_cnt, tp):
            win_cnt += x

ans = win_cnt / total_cnt
print(ans)
