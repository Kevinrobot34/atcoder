# ABC177
* https://atcoder.jp/contests/abc177


## C - Sum of product of pairs (300点)
* keywords
  - 累積和、数式の変形
* 解法
  - 求めるものは`sum(sum(a[:i]) * a[i] for i in range(n))`
  - `sum(a[:i])`を累積和として事前計算するだけ
  - `O(N)`


## D - Friends (400点)
* keyword
  - UnionFind
* 解法
  - UnionFind使い、友達関係で繋がる人たちをつなげる
  - 最もサイズの大きい連結成分の人たちを全て異なるグループに分ければ良い
  - UnionFindの操作を実質定数と思うと`O(N)`


## E - Coprime (500点)
* keywords
  - 数学、GCD、エラトステネスの篩
* 解法
  - pairwise coprimeの判定について
    - エラトステネスの篩的な発想でやる
  - setwise coprimeの判定について
    - `GCD(GCD(a[0], a[1]), a[2]) ....`とやっていくだけ


## F - I hate Shortest Path Problem (600点)
* keyword
  - 
* 解法
