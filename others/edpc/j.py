import sys

sys.setrecursionlimit(10**8)
n = int(input())
a = list(map(int, input().split()))
memo = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]


def f(i, j, k):
    # f(i, j, k) = (さらに0,1,2個の寿司が置かれている皿がi,j,k枚ある場合から始めたときの、寿司がなくなるまでの操作回数の期待値)
    if memo[i][j][k] != -1:
        return memo[i][j][k]
    if i == n:
        return 0
    l = n - i - j - k
    r1 = j * f(i + 1, j - 1, k) / n if j > 0 else 0
    r2 = k * f(i, j + 1, k - 1) / n if k > 0 else 0
    r3 = l * f(i, j, k + 1) / n if l > 0 else 0
    ret = (1 + r1 + r2 + r3) / (1 - i / n)

    memo[i][j][k] = ret
    return ret


ans = f(0, a.count(1), a.count(2))
print(ans)
