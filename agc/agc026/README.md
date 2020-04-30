# AGC026
* https://atcoder.jp/contests/agc026


## A - Colorful Slimes 2 (200点)
* 同じ色のスライムが`x`匹連続して並ぶ区間に注目する
  - `x//2`匹の色を変更すれば良い
  - 例
    - `55555` -> `51515` etc
    - `4444`  -> `4141`  etc
* 前から見て同じ色が連続する区間毎に上記を考えていく


## B - rng_10s (600点)



## C - String Coloring (600点)
* 半分全列挙
  - ハッシュテーブル(Pythonのset/dict)を上手に使う
  - 多分`O(N2^N)`
