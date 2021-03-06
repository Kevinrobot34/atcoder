# ABC170
* https://atcoder.jp/contests/abc170


## C - Forbidden List (300点)
* 解法
  - xから下にずらした場合と上にずらした場合をそれぞれ求め、条件に合う方を出力する


## D - Not Divisible (400点)
* keywords
  - エラトステネスの篩
* 解法
  - `A`はソートしておく
  - `A[i]<=10**6`なので、エラトステネスの篩的なことをする
    - 小さい方から見て、
  - `M=MAX(A)` として `O(MloglongM)` ?


## E - Smart Infants (500点)
* keywords
  - C++のset、平行二分探索木、priority_queue
* Reference
  - [【Python】平衡二分木が必要な時に代わりに何とかするテク【競プロ】]( https://qiita.com/Salmonize/items/638da118cd621d2628d1#%E8%A7%A3%E6%B1%BA%E6%B3%953-%E5%84%AA%E5%85%88%E5%BA%A6%E4%BB%98%E3%81%8D%E3%82%AD%E3%83%A5%E3%83%BC )


## F - Pond Skater (600点)
* keywords
  - BFS、Dijkstra
* 解法1
  - `(x, y, dir)`を状態として持つdijkstra
  - 参考
    - editorial
    - [momoharaさんのコード]( https://atcoder.jp/contests/abc170/submissions/14352039 )
* 解法2
  - DFSをちょっと変更する
  - 参考
    - [chokudaiさんのツイート]( https://twitter.com/chokudai/status/1272168231172632576?s=20 )
    - [chokudaiさんのコード]( https://atcoder.jp/contests/abc170/submissions/14358430 )
* 解法3
  - segtree的に辺を張ってdijkstra
  - 参考
    - [satanic@研究さんの絵]( https://twitter.com/satanic0258/status/1272165396502605824?s=20 )
