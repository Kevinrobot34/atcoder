n, k = map(int, input().split())
sw = [tuple(map(int, input().split())) for _ in range(n)]
sw.sort(key=lambda x: x[1])


def calc(p1, w1, p2, w2):
    return (p1 * w1 + p2 * w2) / (w1 + w2)


used = [False] * n
used[-1] = True
w_sum = sw[-1][0]
p_sum = sw[-1][1]
for i in range(1, k):
    cand = -1
    for j, (wj, pj) in enumerate(sw):
        if used[j]:
            continue
        if cand == -1 or calc(pj, wj, p_sum, w_sum) > calc(
                sw[cand][1], sw[cand][0], p_sum, w_sum):
            cand = j

    p_sum = calc(sw[cand][1], sw[cand][0], p_sum, w_sum)
    w_sum += sw[cand][0]

print(p_sum)
