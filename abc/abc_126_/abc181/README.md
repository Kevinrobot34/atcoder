# ABC181
* https://atcoder.jp/contests/abc181


## C - Collinearity (300点)
* keyword
  - 全探索、数学、平行、幾何
* 解法
  - 任意の3点の組み合わせについて、同一直線上にあるかを全探索するだけ
    - 全探索の部分に `itertools.combinations` を使うとスッキリ書ける
    - 同一直線上かの判定には二次元ベクトルクラスを使ってもいいが、条件をそのまま書いても良かったかも


## D - Hachi (400点)
* keyword
  - 数学、全探索
* 解法
  - 8の倍数である条件は、下3桁が8の倍数となっていること
  - 3桁の8の倍数は高々1000個しかないので、これらを与えられた `S` から作りうるかを全探索するだけ


## E - Transformable Teacher (500点)
* keyword
  - 累積和、二分探索
* 解法
  - 先生の身長を一つ決めてしまえば、生徒とあわせて `N+1` 人をソートして前から2人ずつペアを作るのが最適なことがわかる
  - `h[2*i] - h[2*i-1]` の前からの累積和と後ろからの累積和を持っておいて、二分探索と組み合わせると高速に解ける


## F - Silver Woods (600点)
* keyword
  - UnionFind
* 解法
  - editorialが分かりやすいので読みましょう
  - 二つの直線が同じ連結成分に入ってしまうと、スタート地点とゴール地点を分け隔ててしまうので移動不可能という話
  - 迷路の壁を短いやつから順に増やしていくイメージ
