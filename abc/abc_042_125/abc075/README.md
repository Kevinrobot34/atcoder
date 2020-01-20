# ABC075
* https://atcoder.jp/contests/abc075


## C - Bridge (300点)
* 一つの辺を取り除いた上で、グラフが非連結になるかを愚直に調べれば良い
  - グラフが非連結かどうかを確かめるのはいろんな方法がある
    - UnionFind (`c_uf.py`)
    - DFS
  - どれも大体非連結かどうかの判定にO(N+M)でそれをM回繰り返すのでO(M(N+M))


# D - Axis-Parallel Rectangle (400点)
いくつか解法がある
* 座圧と二次元累積和でO(N^4)
* 愚直な解法でO(N^3)
