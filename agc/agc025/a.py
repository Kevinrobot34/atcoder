n = int(input())


def digit_sum(x):
    return sum(int(si) for si in str(x))


ans = 10**5
for a in range(1, n):
    b = n - a
    ans = min(ans, digit_sum(a) + digit_sum(b))

print(ans)
