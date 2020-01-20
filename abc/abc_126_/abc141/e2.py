def main():
    n = int(input())
    s = input()


    def check(l):
        if l == 0:
            return True
        # for i in range(n-l*2+1):
        i = 0
        while i < n-l*2+1:
            j = i + l
            # for j in range(i+l, n-l+1):
            while j < n-l+1:
                cnt = 0
                # print(i, j)
                for k in range(l):
                    if s[i+k] == s[j+k]:
                        cnt += 1
                    else:
                        break

                if cnt == l:
                    # print(l, i, j, cnt,)
                    return True
                else:
                    j += max(cnt, 1)
            i += 1

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

main()
