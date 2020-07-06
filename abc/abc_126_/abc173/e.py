MOD = 10**9 + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))
am = []
ap = []
for ai in a:
    if ai > 0:
        ap.append(ai)
    elif ai < 0:
        am.append(-ai)
am.sort(reverse=True)
ap.sort(reverse=True)

nm = len(am)
np = len(ap)
nz = n - np - nm
# print(am)
# print(ap)

if np + nm < k:
    ans = 0
elif np == 0:
    if k % 2 == 1:
        if nz > 0:
            ans = 0
        else:
            am.sort()
            ans = -1 + MOD
            for i in range(k):
                ans *= am[i]
                ans %= MOD
    else:
        ans = 1
        for i in range(k):
            ans *= am[i]
            ans %= MOD
elif np < k:
    if (k - np) % 2 == 1:
        idx1 = np - 1
        idx2 = k - np + 1
        if k - np + 1 > nm:
            if nz > 0:
                ans = 0
            else:
                if nm % 2 == 1:
                    ans = -1 + MOD
                else:
                    ans = 1
                for i in range(np):
                    ans *= ap[i]
                    ans %= MOD
                for i in range(nm):
                    ans *= am[i]
                    ans %= MOD
        else:
            while idx1 >= 2 and idx2 + 1 < nm and \
                ap[idx1 - 1] * ap[idx1 - 2] < am[idx2] * am[idx2 + 1]:
                idx1 -= 2
                idx2 += 2
            ans = 1
            for i in range(idx1):
                ans *= ap[i]
                ans %= MOD
            for i in range(idx2):
                ans *= am[i]
                ans %= MOD
    else:
        idx1 = np
        idx2 = k - np
        while idx1 >= 2 and idx2 + 1 < nm and \
            ap[idx1 - 1] * ap[idx1 - 2] < am[idx2] * am[idx2 + 1]:
            idx1 -= 2
            idx2 += 2
        ans = 1
        for i in range(idx1):
            ans *= ap[i]
            ans %= MOD
        for i in range(idx2):
            ans *= am[i]
            ans %= MOD
else:
    idx1 = k
    idx2 = 0
    while idx1 >= 2 and idx2 + 1 < nm and \
        ap[idx1 - 1] * ap[idx1 - 2] < am[idx2] * am[idx2 + 1]:
        idx1 -= 2
        idx2 += 2
    ans = 1
    for i in range(idx1):
        ans *= ap[i]
        ans %= MOD
    for i in range(idx2):
        ans *= am[i]
        ans %= MOD

print(ans)
