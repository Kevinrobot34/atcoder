# ARC023
* https://atcoder.jp/contests/arc023


## B - 謎の人物X
* keywords
  - 偶奇、市松模様
* 解法
  - 各マスがd回の移動で到達できるかを判定するだけ
    - マス`(i, j)`に到達できる条件は以下の2つを満たすこと
      - `i+j <= d`
      - `i+j`と`d`の偶奇が一致している
        - 市松模様にして考えるとわかりやすい
          - 白黒の市松模様でグリッドを塗る
          - 一度の移動で異なる色にしか移動できない的な
        - editorial参照


# C - タコヤ木
* keyword
  - Combination
* 解法
  - `A[i]`が大きな数なので、適当にCombinationの計算していると遅いことに注意