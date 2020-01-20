n = int(input())
s = input()


def check(l):
    if l == 0:
        return True
    for i in range(n-l*2 + 1):
        k = 0
        j = i+l
        while j < n:
            # print(i, j-k, k)
            if s[i+k] == s[j]:
                k += 1
            else:
                if j > n-l + 1:
                    break

                if k > 0:
                    j -= 1

                k = 0

            if k == l:
                # print(l, i, j-k+1, k,)
                return True
            j += 1

    return False

# print(6, check(6))
# print()

lb = 0
ub = n // 2 + 1
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        lb = mid
    else:
        ub = mid

print(lb)
