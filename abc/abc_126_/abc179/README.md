# ABC179
* https://atcoder.jp/contests/abc179


## C - A x B + C (300点)
* keyword
  - 全探索
* 解法
  - AとBを掛け算してN未満であれば対応するCは一意に定まる
  - よって、Aを全探索して掛け算してN未満となるBの数を数えればいいだけ


## D - Leaping Tak (400点)
* keywords
  - セグメントツリー、SegmentTree、RSQ
* 解法1 (editorial)
  - O(NK)
* 解法2
  - DPする
    - `dp[i] = (マスiに移動する方法のMOD)`
  - 更新にRangeSumQueryなセグメントツリーを使う
  - `O(KNlogN)`


## E - Sequence Sum (500点)
* keywords
  - 鳩の巣原理、周期性、ダブリング、シミュレーション
* 解法
  - `A`は次のような遷移をする
    ```
    z -> ... -> a -> b -> ... -> c
                         ↑           ↓
                         e <- ... <- d
    ```
  - `M`での余りを取っているので、上記の遷移に登場する数は高々`M`個
  - よって`O(M)`で計算できる


## F - Simplified Reversi (600点)
* keywords
* 解法
