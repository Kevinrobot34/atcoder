# ABC173
* https://atcoder.jp/contests/abc173


## C - H and V (300点)
* keyword
  - bit全探索
* 解法
  - 行と列それぞれに対してbit全探索するだけ
  - `O(HW2^{H+W})`


## D - Chat in a Circle (400点)
* keyword
  - シミュレーション
* 解法
  - 各人のフレンドリーさ`A[i]`が心地よさに寄与するのはどういう時かを考える
    - 定義通り、ある人の両脇が`A[i]`と`A[j]`で、`A[i] < A[j]`の時
  - また心地よさの合計を最大にしたいので、なるべく大きい`A[i]`を心地よさに寄与させたい
  - `A`をソートして降順にする
    - `A[0]`は1度だけ寄与
    - `A[1]`は2度寄与
    - ...


## E - Multiplication 4 (500点)
* comment
  - 面倒


## F - Intervals on Tree (600点)
* keywords
  - 木、森、連結成分
* 解法
  - `f(L, R)` を考える際に誘導されるグラフは木が集まったもの（つまり、森）
  - 森の性質
    - `(連結成分) = (頂点数) - (辺の数)`
  - これを踏まえ `\sum_L \sum_R f(L, R)` を書き下せば簡単に求められる
* comments
  - [optさんのツイート]( https://twitter.com/opt_coder/status/1280148282161762305?s=20 )
    > ・木の誘導部分グラフは森 \
    > ・森の連結成分数は「頂点数 - 枝数」 \
    > ・和の計算は順序交換可能 \
    > はどれも典型なので，あまりセンスとか発想が要求されず，練習で解けるようになるタイプの問題と感じた (なので解けなくても焦る必要はないと思う)
