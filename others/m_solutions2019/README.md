# M-SOLUTIONS プロコンオープン 2019
* https://atcoder.jp/contests/m-solutions2019


## C - Best-of-(2n-1) (500点)
* keywords
* 解法


## D - Maximum Sum of Minimum (500点)
* keywords
  - グラフ、構築系
* 解法
  - ある適当な頂点を根として根付き木として考える
  - まずスコアの上界として、`sum(c) - max(c)`であることは容易にわかる
  - 以下のようにすることで上記を達成できる
    - 根に`max(c)`を書き込む
    - 木をdfsしながら、`ci`の大きい順に書き込んでいく
      - この塗り方をすると必ず親の数字の方がこの数字以上になる
      - 全ての辺で子の頂点の数字が辺に書き込まれる
