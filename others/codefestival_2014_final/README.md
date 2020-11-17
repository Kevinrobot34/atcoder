# CODE FESTIVAL 2014 決勝
* https://atcoder.jp/contests/code-festival-2014-final


## C - N進数
* keyword
  - N進数、数学、全探索
* 解法
  - `k=10`から順番に`f(k)`が`A`以上となるまで全探索する
  - `f(k)`は`O(k^logk)`なので、`10^5`くらいまで調べればいいことが分かる


## D - パスカルの三角形
* keyword
  - 構築系
* 解法
  - `(a+1, 2)`を返すだけ（なんだそれ


## E - 常ならずグラフ
* keywords
  - 貪欲法、DP
* 解法1
  - 貪欲法
  - 数列の形の候補
    - x1 < x2 > x3 < x4 > ...
    - x1 > x2 < x3 > x4 < ...
  - 元の数列の内、単調増加or減少となってる部分について、その部分の両端以外を削れば良い
  - `O(N)`
  - https://imulan.hatenablog.jp/entry/2015/10/28/215848
* 解法2
  - DPする（自分の解法）
  - `O(N^2)`
