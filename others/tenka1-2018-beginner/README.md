# Tenka1 Programmer Beginner Contest 2018
* https://atcoder.jp/contests/tenka1-2018-beginner


## C - Align (400点)
* keywords
  - 貪欲
* 解法1
  - 基本的に大きい数の両脇に小さい数を、小さい数の両脇に大きい数を置きたい
  - dequeを使って上記を貪欲に構成してみる
* 解法2(editorial)
  - 「大小大小...」か「小大小大...」か、どちらかの並べ方にするのが良い
  - 前者について例えば `n=4` の場合
    - `(a[0] - a[1]) + (a[2] - a[1]) + (a[2] - a[3])`
    - つまり `a[0] + (-2)*a[1] + 2*a[2] + (-1)*a[3]`
  - 上記の係数だけ考えて、大きい数から割り振れば良い
  - https://drken1215.hatenablog.com/entry/2018/10/28/222800


## D - Crossing (500点)
* keywords
  - 構築系
* 解法(editorial)
  - 
