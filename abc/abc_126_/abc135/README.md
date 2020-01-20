# ABC135
* https://atcoder.jp/contests/abc135


## C - City Savers 2019 (300点)
貪欲に計算


## D - Digits Parade (400点)
DP


## E - Golf (500点)



## F - Strings of Eternity (600点)
* 文字列`s`(`t`よりは長くなるように拡張)の`i`文字目から`|t|`文字分が文字列`t`と一致しているかどうかを判定する。
  - Z-z_algorithm
    - https://snuke.hatenablog.com/entry/2014/12/03/214243
  - KMP法
    - https://snuke.hatenablog.com/entry/2017/07/18/101026
  - Rolling Hash
* 上記の判定で一致していたら、`i`から`(i+|t|)%|s|`に辺を貼り、有向グラフを構築する。これの最長パスを求める
  - topological_sortしてdagか判定ののち、適当にDP
  - UnionFind(１頂点から伸びてる辺が１つのみだから使える)
