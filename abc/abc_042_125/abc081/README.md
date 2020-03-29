# ABC081
* https://atcoder.jp/contests/abc081


## C - Not so Diverse (300点)
数えて、ソートする


## D - Non-decreasing (600点)
* まず全て正の数からなる数列を考える
  - この場合前から、「`a[i]`を`a[i+1]`に加える」という操作をN-1回行うと、条件を満たせていることが分かる。
  - 累積和みたいな
* 全て負の数からなる数列も同様
* 正負混ざっている数列が面倒
  - もしもminの絶対値よりもmaxが大きいなら、全ての負の数に最大値を足す操作（高々N-1回）を繰り返せば全ての要素を正にできる
  - 続いて上記の累積和をとるような操作をN-1回やれば条件を満たせる