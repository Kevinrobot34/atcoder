# WUPC 2012
* https://atcoder.jp/contests/wupc2012


## E - 会場への道
* keywords
  - グラフ、Dijkstra、頂点倍加
* 解法
  - `(町i, 町iに到着した時間を28で割った余り)` が頂点となるように倍加してDijkstra
  - 「会場に到着してから引き返してはいけない」に注意
    - 町`n-1`に対応する頂点からは辺を伸ばさなければ良い
