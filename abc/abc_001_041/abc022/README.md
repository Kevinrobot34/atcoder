# ABC022
* https://atcoder.jp/contests/abc022


## C - Blue Bird
* 最短閉路問題?ともいうべき問題
* スタートの頂点1と隣接する頂点x, yを通る閉路を考える
  - 閉路の長さは`(1->x) + (x->y) + (y->1)`
* 片方の端点が1であるような辺を全て取り除き、`(x->y)`の最短経路をwarshal-floydで求める
  - これは最短経路なので同じ道を二度通ったりはしない
  - `(1->x)`と`(y->1)`とは必ず異なる辺からなる経路
* 任意の1と隣接する`x, y`に対して、`(1->x) + (x->y) + (y->1)`が最小となるものを探す


## D - Big Bang
