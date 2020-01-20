from collections import defaultdict

n, k = map(int, input().split())
sushi = [list(map(int, input().split())) for _ in range(n)]

sushi.sort(key=lambda x: -x[1])
# print(sushi)

kinds = defaultdict(list)
remove_candidates = []
umami = 0

ans_candidates = {}
for i in range(n):
    t, d = sushi[i]
    # print("t, d = ", t, d)
    if i < k:
        if t in kinds:
            remove_candidates.append(d)
        kinds[t].append(i)
        umami += d
    elif t not in kinds and len(remove_candidates) > 0:
        kinds[t].append(i)
        x += 1
        d2 = remove_candidates.pop()
        umami = umami - d2 + d
        ans_candidates[x] = umami + x * x
        # print("remove", remove_candidates)
        # print(x, umami, ans_candidates[x])

    if i == k - 1:
        x = len(kinds.keys())
        ans_candidates[x] = umami + x * x
        remove_candidates.sort(key=lambda x: -x)
        # print(umami)
        # print(kinds, x)
        # print(remove_candidates)
        # print(x, umami, ans_candidates[x])

# print()
# print(ans_candidates)
print(max(ans_candidates.values()))
