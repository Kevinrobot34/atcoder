# ARC111
* https://atcoder.jp/contests/arc111


## A - Simple Math 2 (300点)
* keyword
  - 数学、繰り返し二乗法
* 解法1
  - 繰り返し二乗法でやる
* 解法2(editorial)
  - 数学
  - 数式変形すると `pow(10, n, m**2)` の `m` で割った商が答え


## B - Reversible Cards (400点)
* keyword
  - グラフ、連結成分、UnionFind
* 解法
  - editorialの通り
  - UnionFindをちょっと変形して連結成分ごとに頂点と辺の数を管理すれば簡単に解ける
  - もちろんDFSしてもOK
