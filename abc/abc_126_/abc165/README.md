# ABC165
* https://atcoder.jp/contests/abc165


## C - Many Requirements (300点)
* keyword
  - 全探索, DFS, combinations_with_replacement
* 解法１
  - DFSで全探索
* 解法２
  - [itertools.combinations_with_replacement]( https://docs.python.org/ja/3/library/itertools.html#itertools.combinations_with_replacement )


## D - Floor Function (400点)
* keyword
  - floor, 切り捨て, 数学
* 解法
  - `x=B*i`だと0になることがすぐに分かる
  - `x=B*i+r (0<=r<B)`と置く
    - `i`由来の項は相殺される事もわかる
    - 更に`floor(r/B)`は0
    - 第１項はxの非減少関数なので、`x=min(B-1, N)`が答え


## E - Rotation Matching (500点)
* keyword
  - 構築
* 解法
  - 入出力例１みたいな形でたくさん実験してみる
    - Aさんに注目して、誰と対戦するかを見ていけば良い
  - ある対戦場に割り当てた２つの数の差(`abs(a-b)`)に注目する
    - 差が`i`の時、Aさんは`i`人前の人と`i`人後ろの人と対戦することになる
    - よって対戦場に割り当てた２つの数の差は、全ての対戦場で相異なるはず
    - あとはこれを上手に配置する方法を考えるだけ


## F - LIS on Tree (600点)
* keyword
  - DP, LIS, 木, 巻き戻し
* 解法
  - 木の上でLISを求める問題
  - dfsし終わったら、巻き戻す
* コメント
    * オイラーツアー使ったと言ってる人も見かけた（マジ！？
    * LIS系の問題
        * [ABC006 D - トランプ挿入ソート]( https://atcoder.jp/contests/abc006/tasks/abc006_4 )
            * 蟻本的実装 : [これ]( https://atcoder.jp/contests/abc006/submissions/12671707 )
            * Listを使った実装 : [これ]( https://atcoder.jp/contests/abc006/submissions/7025956 )
            * BIT使った実装 : まだ
                * ABC038Dに近いやり方
                * 参考 : https://noshi91.hatenablog.com/entry/2018/02/03/204950
        * [ABC038 D - プレゼント]( https://atcoder.jp/contests/abc038/tasks/abc038_d )
            * DPの漸化式の更新にRangeMaximumQuery(SegmentTree/BIT)を使う
        * [ABC134 E - Sequence Decomposing (500点)]( https://atcoder.jp/contests/abc134/tasks/abc134_e )
