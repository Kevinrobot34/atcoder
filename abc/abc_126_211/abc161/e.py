n, k, c = map(int, input().split())
s = list(input())
# print(s)

dp1 = [0] * (n + 1)
for i in reversed(range(n)):
    j = min(i + c + 1, n)
    if s[i] == 'o':
        dp1[i] = max(dp1[j] + 1, dp1[i + 1])
    else:
        dp1[i] = max(dp1[j], dp1[i + 1])

dp2 = [0] * (n + 1)
for i in range(n):
    j = max(i - c - 1, -1)
    if s[i] == 'o':
        dp2[i] = max(dp2[j] + 1, dp2[i - 1])
    else:
        dp2[i] = max(dp2[j], dp2[i - 1])

# print(dp1)
# print(dp2)


def check(idx):
    if s[idx] == 'x':
        return False

    if dp1[idx + 1] + dp2[idx - 1] >= k:
        return False
    else:
        return True


for i in range(n):
    if check(i):
        print(i + 1)
