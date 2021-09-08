# ABC189
* https://atcoder.jp/contests/abc189


## C - Mandarin Orange (300点)
* keywords
  - 極大長方形、スタック
* 解法1
  - ナイーブな解法は`O(N^3)`で、もちろんTLE
  - 区間minを取る処理にセグメントツリーを使えば`O(N^2 logN)`で、これもTLE
  - 区間minを取るところを累積minを取るような処理にすることで`O(N^2)`
* 解法2
  - 極大長方形と呼ばれるようなスタックを利用した`O(N)`のアルゴリズム
  - `c2.py`がアリ本通りの実装
  - `c3.py`の実装
    - https://zenn.dev/yamasakit/articles/c64b433b116179


## D - Logical Expression (400点)
* keywords
  - DP
* 解法
  - 動的計画法をやる
    - `dp1[i] = (y[i]がTrueとなるような変数の組みの数)`
    - `dp2[i] = (y[i]がFalseとなるような変数の組みの数)`


## E - Rotate and Flip (500点)
* keywords
  - 数学、アフィン変換、クエリ先読み
* 解法
  - クエリと操作を先読みして、各クエリに行列を一度掛けるだけで答えが求められるようにしておく


## F - Sugoroku2 (600点)
* keywords
  - 期待値DP、累積和、二分探索
* 解法1
  - 一次式を持つDP
* 解法2
  - 二分探索
