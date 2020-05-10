import copy
n, k = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

now = 0
while k > 0:
    if k & 1:
        now = a[now]

    a_next = [-1] * n
    for i in range(n):
        a_next[i] = a[a[i]]

    a = copy.copy(a_next)
    k = k >> 1

ans = now + 1
print(ans)
