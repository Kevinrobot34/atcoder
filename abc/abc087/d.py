import math
import copy
from operator import mul
from functools import reduce
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
# 一次元累積和
from itertools import accumulate
from bisect import bisect_left, bisect_right

import re
# import numpy as np
# from scipy.misc import comb

import sys
sys.setrecursionlimit(10**9)

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
def line_inpl(x): return [i_inpl() for _ in range(x)]

INF = int(1e18)
MOD = int(1e9)+7 # 10^9 + 7

# field[H][W]
def create_grid(H, W, value = 0):
    return [[ value for _ in range(W)] for _ in range(H)]

########

def main():
    N, M = l_inpl()

    G = [[] for _ in range(N+1)]

    for _ in range(M):
        Li, Ri, Di = l_inpl()
        Li, Ri = Li - 1, Ri - 1
        G[Li].append((Ri, Di))
        G[Ri].append((Li, -Di))

    # ある点からの距離
    x = [INF] * (N+1)

    # 計算によって得たx[s]が正しいか
    def dfs(s, cost):
        # node_startまでの距離が未探索
        if x[s] == INF:
            x[s] = cost
            # s->tの距離の整合性
            for t, d in G[s]:
                if dfs(t, cost + d) == False:
                    return False
        return x[s] == cost

    for i in range(N):
        # if x[i] is not None: # 探索済み
        #     continue
        if x[i] == INF and dfs(i, 0) == False:
            print("No")
            return
    print("Yes")

if __name__ == "__main__":
    main()
