def main():
    import sys
    input = sys.stdin.readline

    n = int(input())

    L_MAX = 10**5
    D_TH = 10
    V_MAX = (1 << D_TH) - 1
    dp = [[0] * (L_MAX + 1)]
    # items = []
    items_v = []
    items_w = []

    for i in range(n):
        val, w = map(int, input().split())
        if i < V_MAX:
            i1 = i + 1
            i0 = (i + 1) >> 1
            dp_ = dp[i0][:]

            # for j in range(w):
            #     dp[i1][j] = dp[i0][j]
            for j in range(w, L_MAX + 1)[::-1]:
                if dp_[j] < dp_[j - w] + val:
                    dp_[j] = dp_[j - w] + val
            dp.append(dp_)
        else:
            # items.append((val, w))
            items_v.append(val)
            items_w.append(w)

    # items = tuple(items)

    q = int(input())
    for _ in range(q):
        v, l = map(int, input().split())
        v -= 1

        if v < V_MAX:
            ans = dp[v + 1][l]
        else:
            vv = []
            ww = []
            while v >= V_MAX:
                # vv.append(items[v - V_MAX][0])
                # ww.append(items[v - V_MAX][1])
                vv.append(items_v[v - V_MAX])
                ww.append(items_w[v - V_MAX])
                v = (v - 1) >> 1

            ans = dp[v + 1][l]
            # m = len(vv)
            m2 = 1 << len(vv)
            v_sub = [0] * m2
            w_sub = [0] * m2
            for bit in range(1, m2):
                bit_min = bit & (-bit)
                x = bit_min.bit_length() - 1

                s_w = w_sub[bit - bit_min] + ww[x]
                w_sub[bit] = s_w
                if s_w <= l:
                    s_val = v_sub[bit - bit_min] + vv[x]
                    v_sub[bit] = s_val
                    ans = max(ans, dp[v + 1][l - s_w] + s_val)

        print(ans)


if __name__ == '__main__':
    main()
