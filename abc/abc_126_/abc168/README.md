# ABC168
* https://atcoder.jp/contests/abc168


## C - : (Colon) (300点)
* keywords
  - 数学、余弦定理
* 解法
  - 余弦定理を使って計算するだけ
* comment
  - 久しぶりに余弦定理とか使った


## D - .. (Double Dots) (400点)
* keywords
  - dijkstra、経路復元
* 解法1
  - dijkstraして、経路復元用の `prev_node` が答えになる
  - Noは無いよねっていう
* 解法2
  - BFS
  - 直前のnodeを保存しておく


## E - ∙ (Bullet) (500点)
* keywords
  - 数え上げ、角度
* 解法
  - ab平面の上半平面にまとめちゃう
  - `(1, 1)` と `(2, 2)` は同一視する
  - 90度をなすペアはどちらかの角度のベクトルしか利用できない
    - ベクトルごとに独立に考えられる
  - `(0, 0)` だけ扱いが違うことに注意


## F - . (Single Dot) (600点)
* keywords
  - 幾何、面積、軸と平行、座標圧縮
