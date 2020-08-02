# ABC174
* https://atcoder.jp/contests/abc174


## C - Repsept (300点)
* keyword
  - 数学、シミュレーション
* 解法
  - 与えられた数列を`{a[i]}`とする
  - 上記を`K`で割った余りの数列を`{b[i] = a[i] % K}`とする
  - `b[i+1] = (10 * b[i] + 7) % K`
  - この数列`b`は高々周期`K`の数列なので、シミュレーションで全部求められる
  - その上で途中で0となることがあるかを確かめれば良い
  - `O(K)`


## D - Alter Altar (400点)
* keyword
  - 累積和
* 解法
  - 最終的に`RR...RWW...W`とすれば良い
  - とりあえず左に`R`を`i`個、右に`W`を`n-i`個を目指すとする
    - 境界より左に`W`が`x`個あり、右に`R`が`y`個あるとする
    - `max(x, y)`回の操作で達成可能
      - まず`min(x, y)`回、境界より左の`W`と右の`R`を交換する
      - 次に残った`max(x, y) - min(x, y)`の石の色を反転させる
  - 上記の`x`と`y`は累積和を使えば`O(1)`で求められる
  - よって`RW`の境界を全探索すれば良い
  - `O(N)`


## E - Logs (500点)
* keywords
  - 二分探索
* 解法
  - 「最大値の最小化」をする典型的な二分探索の問題
  - check関数について
    - 「任意の丸太を`K`回の操作で`x`以下にできるか」を判定する
    - `K`が大きいのでそのままシミュレーションみたいなことはできない
    - そこで「任意の丸太を`x`以下にするためには操作は何回必要か」を考える
      - ある丸太`a[i]`について、丸太を切って行って何回で全てを`x`以下にできるか？
      - `(a[i] - 1) // x`回
* comments
  - 『「最大値の最小化」をする典型的な二分探索の問題』であることはすぐ分かったが、なんか時間かかってしまった


## F - Range Set Query (600点)
* keywords
  - BIT
* 解法1
  - Google検索して ["Queries for number of distinct elements in a subarray"]( https://www.geeksforgeeks.org/queries-number-distinct-elements-subarray/ ) を見つける
* comments
  - Google検索力勝負...
