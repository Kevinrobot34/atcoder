# ABC183
* https://atcoder.jp/contests/abc183


## C - Travel (300点)
* keywords
  - 全探索、順列、N!
* 解法
  - `N!` 通りの全探索
  - `from itertools import permutations` すれば簡単


## D - Water Heater (400点)
* keywords
  - imos法
* 解法
  - imos法するだけ


## E - Queen on Grid (500点)
* keywords
  - DP、経路数、累積和
* 解法
  - 経路数を数えるよくあるDPを拡張したような問題
    - 右・下のみならず、右下も動ける
    - 一度の移動で壁にぶつかるまでどこまでも行ける
  - 累積和を取りながらDPをする感じ


## F - Confluence (600点)
* keywords
  - UnionFind、拡張
* 解法
  - マージテクニックを使ったUnionFindにクラス毎の人数の情報を載せる
  - マージするときにクラス毎の人数の情報を更新する
    - 毎回rootの頂点のdefaultdictを更新する
    - マージテクにより、小さい方のdict分しかループを回さないのでまあ間に合う(?)
