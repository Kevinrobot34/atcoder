from collections import Counter
n, k = map(int, input().split())
s = input()
s_cnt = Counter(list(s))
s_char = sorted(list(s))
used = [False] * n

# print(s_char)
# print(s_cnt)


def count_common_char(s1_cnt, s2_cnt):
    cnt = 0
    for k, v in s1_cnt.items():
        if k not in s2_cnt:
            continue
        cnt += min(v, s2_cnt[k])
    return cnt


ans = ''
for i in range(n):
    for j, c in enumerate(s_char):
        if used[j]:
            continue

        s_cnt[c] -= 1
        ans += c
        cnt1 = i + 1 - sum([1 for k in range(i + 1) if s[k] == ans[k]])
        cnt2 = n - 1 - i - count_common_char(s_cnt, Counter(list(s[i + 1:])))
        # print(ans, s[:i + 1], cnt1, cnt2)
        if cnt1 + cnt2 <= k:
            used[j] = True
            break
        s_cnt[c] += 1
        ans = ans[:-1]
print(ans)
