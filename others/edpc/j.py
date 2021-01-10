from collections import Counter
n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
memo = {}


def f(i, j, k):
    # f(i, j, k) = (さらに0,1,2個の寿司が置かれている皿がi,j,k枚ある場合の)
    if (i, j, k) in memo:
        return memo[(i, j, k)]
    if i == n:
        return 0
    l = n - i - j - k
    r1 = j * (f(i + 1, j - 1, k) + 1) if j > 0 else 0
    r2 = k * (f(i, j + 1, k - 1) + 1) if k > 0 else 0
    r3 = l * (f(i, j, k + 1) + 1) if l > 0 else 0
    ret = (i / n) / ((1 - i / n)**2) * (r1 + r2 + r3) / n

    memo[(i, j, k)] = ret
    return ret


ans = f(0, cnt[1], cnt[2])
print(memo)
print(ans)
