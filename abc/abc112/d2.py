import math
n, m = map(int, input().split())


def divisor(m):
    ans = []
    for i in range(1, int(math.sqrt(m)) + 1):
        if m % i == 0:
            ans.append(i)
            ans.append(m // i)

    return sorted(ans)


divs = divisor(m)
j = len(divs) - 1
while True:
    if divs[j] * n <= m:
        print(divs[j])
        break
    j -= 1
