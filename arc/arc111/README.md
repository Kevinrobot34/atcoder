# ARC111
* https://atcoder.jp/contests/arc111


## A - Simple Math 2 (300点)
* keywords
  - 数学、繰り返し二乗法
* 解法1
  - 繰り返し二乗法でやる
* 解法2(editorial)
  - 数学
  - 数式変形すると `pow(10, n, m**2)` の `m` で割った商が答え


## B - Reversible Cards (400点)
* keywords
  - グラフ、連結成分、UnionFind
* 解法
  - editorialの通り
  - UnionFindをちょっと変形して連結成分ごとに頂点と辺の数を管理すれば簡単に解ける
  - もちろんDFSしてもOK


## E - Simple Math 3 (800点)
* keywords
  - 数学、floor_sum
* 解法
  - 条件のおさらい
    - `1 <= A < D`
    - `0 <= B < C < D`
    - `2 <= D < 10**8`
  - 重要事実
    - [A] 以下が同値であること
      - `Y <= x <= Z` なる任意の`x`は`D`の倍数ではない
      - `Y=D*q+r_y`かつ`Z=D*q+r_z`（ただし`q`は整数かつ`1 <= r_y <= r_z < D`）
      - `floor((Y-1)/D) = floor(Z/D)`
    - [B] 一般に`Y<=Z`かつ`Z-Y<D`の時、`floor(Z/D) - floor((Y-1)/D)`は0または1 [A]
  - 事実[A]と同様に問題分の条件も同値変形する
    - 「`A+B*i`以上`A+C*i`以下の整数はいずれも`D`の倍数ではない」ような正整数`i`の数
    - 「`A+B*i <= x <= A+C*i`なる任意の`x`は`D`の倍数ではない」ような正整数`i`の数
    - 「`floor((A+B*i - 1) / D) = floor((A+C*i) / D)` である」ような正整数`i`の数
  - `(A+C*i) - (A+B*i) = (C-B)*i`が`D-1`以上の時は常に条件は満たされない
    - よって `1 <= i <= (D-2) / (C-B)`の範囲で考えれば良い
    - `K = (D-2) / (C-B)`とする
  - 以上より求める数は以下のように書き換えられる
    - `floor((A+B*i - 1) / D) = floor((A+C*i) / D)`なる`1<=i<=K`の数
    - `sum(1 - ( floor((A+C*i) / D) - floor((A+B*i - 1) / D) ) | 1<=i<=K)`
      - 事実[B]より
    - `K - sum( floor((A+C*i) / D) - floor((A+B*i - 1) / D) | 1<=i<=K)`
    - `K - sum( floor((A+C*i) / D) - floor((A+B*i - 1) / D) | 0<=i<K+1)`
      - `floor(A/D) = floor((A-1)/D) = 0`なので
    - `K - sum( floor((A+C*i) / D) | 0<=i<K+1) + sum( floor((A+B*i - 1) / D) | 0<=i<=K+1)`
    - `K - sum( floor((C*i + A) / D) | 0<=i<K+1) + sum( floor((B*i+ A-1) / D) | 0<=i<=K+1)`
      - このそれぞれの和はfloor_sumで求められる
