# ABC157
* https://atcoder.jp/contests/abc157


## C - Guess The Number (300点)
* 解法１
  - N桁の数を小さい方から全探索
* 解法２
  - M個の条件を満たすものを列挙
  - N=1の時は0が最小なことに注意


## D - Friend Suggestions (400点)
* https://atcoder.jp/contests/abc157/submissions/10442112
* Union Find


## E - Simple String Queries (500点)
* 解法１ : O(N + 26 Q log N)
  - https://atcoder.jp/contests/abc157/submissions/10456703
  - アルファベットの数のBITを用意して、区間`[1, i]`にそのアルファベットがいくつあるかをカウントする
* 解法２ : O(N log N + N + Q log N)
  - https://atcoder.jp/contests/abc157/submissions/10477209
  - BitSetを載せたSegmentTree
  - 計算量
    - BitSetの準備 `O(N log N)`
    - Segtreeの構築 `O(N)`
    - query `O(Q log N)`
* 解法３
  - C++のsetを使う


## F - Yakiniku Optimization Problem (600点)
* 二分探索 : O(N^3 log (100*2000 / 1e-6) )
  -
