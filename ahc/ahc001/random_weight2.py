import random

SEED = 2021
N_TRIAL = 11 * 10**6
L_FIELD = 10000


def sum_v(x, y):
    return [xi + yi for xi, yi in zip(x, y)]


def calc_area(x):
    return (x[2] - x[0]) * (x[3] - x[1])


def is_overlapped(x, y):
    if x[2] <= y[0] or y[2] <= x[0] or x[3] <= y[1] or y[3] <= x[1]:
        return False
    else:
        return True


def calc_score(ans, xyr):
    score = 0.0
    for i, ans_i in enumerate(ans):
        si = calc_area(ans_i)
        ri = xyr[i][2]
        score += 1 - (1 - min(si, ri) / max(si, ri))**2
    score /= len(xyr)
    return score


def main():
    random.seed(SEED)

    # input
    n = int(input())
    xyr = [list(map(int, input().split())) for _ in range(n)]
    w = [ri**0.75 + 100 for _, _, ri in xyr]

    ans = [(xi, yi, xi + 1, yi + 1) for xi, yi, _ in xyr]

    dd = [
        (-1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, +1, 0),
        (0, 0, 0, +1),
    ]
    dir = [[True] * 4 for _ in range(n)]
    is_large = [False] * n
    index_list = list(range(n))

    i_list = random.choices(index_list, w, k=N_TRIAL)
    k_list = random.choices(list(range(4)), k=N_TRIAL)

    for i, k in zip(i_list, k_list):
        # i = random.choices(index_list, w)[0]
        if is_large[i]:
            continue

        if not dir[i][k]:
            continue

        v = sum_v(ans[i], dd[k])
        if calc_area(v) > xyr[i][2]:
            is_large[i] = True
            # _index = index_list.index(i)
            # index_list.pop(_index)
            # w.pop(_index)
            continue
        if v[0] < 0 or v[1] < 0 or v[2] >= L_FIELD or v[3] >= L_FIELD:
            continue

        is_possible = True
        for j in range(n):
            if i == j:
                continue
            if is_overlapped(ans[j], v):
                is_possible = False
                break

        if is_possible:
            ans[i] = v
        else:
            dir[i][k] = False

    # output
    # print(calc_score(ans, xyr))
    for ans_i in ans:
        print(*ans_i)


main()
