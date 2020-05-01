k, n = map(int, input().split())
num = '123456789'
words = []
for _ in range(n):
    v, w = input().split()
    v = list(map(lambda x: int(x) - 1, list(v)))
    words.append((v, w))
# print(words)


def check(len_list):
    ans = [''] * k
    for v, w in words:
        if sum(len_list[vi] for vi in v) != len(w):
            return False, []
        idx = 0
        for vi in v:
            cand = w[idx:idx + len_list[vi]]
            idx += len_list[vi]
            if len(ans[vi]) == 0:
                ans[vi] = cand
            else:
                if ans[vi] != cand:
                    return False, []

    return True, ans


for bit in range(3**k):
    len_list = [(bit // pow(3, i)) % 3 + 1 for i in range(k)]
    # print(len_list)
    possible, ans = check(len_list)
    if possible:
        break

print(*ans, sep='\n')
