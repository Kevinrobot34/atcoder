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
  - グリッド、面積、軸と平行、座標圧縮、連結成分、UnionFind
* 解法１
  - X/Y座標それぞれに対して座標圧縮する
    - `-INF`と`0`と`INF`の追加を忘れずに
  - 線分をいもす法的に作っておく
  - セルを走査し、線分の有無を元にUnionFindで連結
    - あるセルの右と下のセルに対して判定を行う
  - 全セルを走査し、`(0, 0)`と同じ連結成分を行っているセルについて、各セルの面積を足していく
* 解法２
  - 連結成分の作成にUnionFindではなくBFSを使う
    - DFSでもいい気がするが、TLEした
* References
  - [kmjp's blog]( https://kmjp.hatenablog.jp/entry/2020/05/17/1030 )
  - [maspy's blog]( https://maspypy.com/atcoder-%E5%8F%82%E5%8A%A0%E6%84%9F%E6%83%B3-2020-05-18abc-168 )
    - 図がわかりやすい
    - グリッドを作る
      - グリッドの座標軸の線を0-indexedで数を振る
      - セルは左上の点を代表して呼ぶ
