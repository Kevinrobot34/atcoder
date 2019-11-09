# ARC008
* https://atcoder.jp/contests/arc008


## A - たこ焼き買えるかな？


## B - 謎のたこ焼きおじさん


## C - THE☆たこ焼き祭り2012


## D - タコヤキオイシクナール
* 座標圧縮
* segtree
  - `f_{a,b}(x) = a*x+b`と定義する
  - `S = { f_{a, b} | a, b \in R}`と定義する
  - 集合`S`は関数の合成に関してモノイドをなす
    - 単位元は`f_{1, 0}`
  - `f_{a,b}`を決定する`(a,b)`を要素として持つセグツリーを作る
  - 今回の関数の合成は交換法則を満たさないので、operation_funcを定義する時、順序に注意すること
* tupleのindexでのアクセス or lambda式は遅いらしい...
  - https://atcoder.jp/contests/arc008/submissions/8375652
  - https://atcoder.jp/contests/arc008/submissions/8375645
