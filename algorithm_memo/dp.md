動的計画法 - Dynamic Programming のまとめ

メモ化再帰とか漸化式立てて解くやつ。
[Educational DP Contest]( https://atcoder.jp/contests/dp )とか練習になりそうだし解きたい


## 簡単なやつ
* フィボナッチ数列の延長
  * [ABC129 C - Typical Stairs (300点)]( https://atcoder.jp/contests/abc129/tasks/abc129_c )


## ナップザック問題系
* ナップザック問題系
    * 01ナップザック
        * [ABC015 D - 高橋くんの苦悩]( https://atcoder.jp/contests/abc015/tasks/abc015_4 )
        * [ABC032 D - ナップサック問題]( https://atcoder.jp/contests/abc032/tasks/abc032_d )
        * [ABC060 D - Simple Knapsack (400点)]( https://atcoder.jp/contests/abc060/tasks/arc073_b )
        * [ARC042 C - おやつ]( https://atcoder.jp/contests/arc042/tasks/arc042_c )
        * [東京海上日動コン2020 D - Knapsack Queries on a tree (700点)]( https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_d )
            * 木の上で、半分全列挙を使ったナップザック問題を解く問題
    * 個数制限無しナップザック
        * [ABC153 E - Crested Ibis vs Monster (500点)]( https://atcoder.jp/contests/abc153/tasks/abc153_e )
    * [ABC145 E - All-you-can-eat (500点)]( https://atcoder.jp/contests/abc145/tasks/abc145_e )


## 部分和問題
* 部分和問題
    * 解き方
        * ナップザック的なDP
        * 半分全列挙
    * [TDPC A - コンテスト]( https://atcoder.jp/contests/tdpc/tasks/tdpc_contest )
    * [ARC017 C - 無駄なものが嫌いな人]( https://atcoder.jp/contests/arc017/tasks/arc017_3 )
        * DPは無理で半分全列挙する
    * [ABC159 F - Knapsack for All Segments (600点)]( https://atcoder.jp/contests/abc159/tasks/abc159_f )
        * 部分和のDPの拡張、累積和
    * [ABC169 F - Knapsack for All Subsets (600点)]( https://atcoder.jp/contests/abc169/tasks/abc169_f )


## LIS
* [LIS - 最長増加部分列]( https://github.com/Kevinrobot34/atcoder/blob/master/algorithm_memo/LIS.md )

* LIS (Longest Increasing Subsequence)系
    * [ABC006 D - トランプ挿入ソート]( https://atcoder.jp/contests/abc006/tasks/abc006_4 )
        * 蟻本的実装 : [これ]( https://atcoder.jp/contests/abc006/submissions/12671707 )
        * Listを使った実装 : [これ]( https://atcoder.jp/contests/abc006/submissions/7025956 )
        * BIT使った実装 : まだ
            * ABC038Dに近いやり方
            * 参考 : https://noshi91.hatenablog.com/entry/2018/02/03/204950
    * [ABC038 D - プレゼント]( https://atcoder.jp/contests/abc038/tasks/abc038_d )
        * DPの漸化式の更新にRangeMaximumQueryを使う
    * [ABC134 E - Sequence Decomposing (500点)]( https://atcoder.jp/contests/abc134/tasks/abc134_e )
    * [ABC165 F - LIS on Tree (600点)]( https://atcoder.jp/contests/abc165/tasks/abc165_f )
        * その名の通り、木上でLISをやる
        * 木上といいつつ、「巻き戻し」というテクニックを使うだけなので木DPとはちょっと違うか

## DAG上のDP
* DAG上のDP
    * [ABC144 F - Fork in the Road (600点)]( https://atcoder.jp/contests/abc144/tasks/abc144_f )


## bitDP
整数の2進数表記を用いて、サイズNの部分集合を全列挙するなどして行うDPのこと。

例
* 巡回セールスマン問題(TSP)

問題
* [JOI Flag]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0559 )
* [ABC041 D - 徒競走]( https://atcoder.jp/contests/abc041/tasks/abc041_d )
* [ABC113 D - Number of Amidakuji (400点)]( https://atcoder.jp/contests/abc113/tasks/abc113_d )
* [ABC142 E - Get Everything (500点)]( https://atcoder.jp/contests/abc142/tasks/abc142_e )


## 桁DP
```
dp[i][smaller] :=
  * (smaller = 0) 上からi桁がsと完全一致してる範囲の数で条件を満たしている数
  * (smaller = 1) 上からi桁が既にsより小さい範囲の数で条件を満たしている数
```

### References
* http://drken1215.hatenablog.com/entry/2019/02/04/013700
* https://torus711.hatenablog.com/entry/20150423/1429794075

### Problems
* [Zigzag Numbers]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0570 )
* [ABC007 D - 禁止された数字]( https://atcoder.jp/contests/abc007/tasks/abc007_4 )
* [ABC029 D - 1]( https://atcoder.jp/contests/abc029/tasks/abc029_d )
* [ABC154 E - Almost Everywhere Zero (500点)]( https://atcoder.jp/contests/abc154/tasks/abc154_e )
* xor系
  * 2進数表記で、桁ごとに考えると良いことが多い
  * [ABC117 D - XXOR (400点)]( https://atcoder.jp/contests/abc117/tasks/abc117_d )
  * [ABC129 E - Sum Equals Xor (500点)]( https://atcoder.jp/contests/abc129/tasks/abc129_e )
      * http://drken1215.hatenablog.com/entry/2019/06/10/150000

## 木DP
根付き木上でのDPのこと
* `dp[i] := 頂点iを根とする部分木についての何か`
* ある頂点`i`の`dp[i]`は、その子にあたる頂点`u`らの`dp[u]`から計算できるという状況
  <img title='tree.png' src='/attachments/289ddb21-98c6-450e-931c-2b3183b4da75' width="362" data-meta='{"width":362,"height":164}'>

### 全方位木DP / ReRooting
木の直径を求める時などに使える。
* [†全方位木DP†について - ei1333の日記]( https://ei1333.hateblo.jp/entry/2017/04/10/224413 )


### References
* [競技プログラミングにおける木DP問題まとめ]( https://www.hamayanhamayan.com/entry/2017/06/19/161741 )

### Problems
* [ABC036 D - 塗り絵]( https://atcoder.jp/contests/abc036/tasks/abc036_d )
* [ABC133 E - Virus Tree 2 (500点)]( https://atcoder.jp/contests/abc133/tasks/abc133_e )
* [ARC028 C - 高橋王国の分割統治]( https://atcoder.jp/contests/arc028/tasks/arc028_3 )
* 全方位木DP / Rerooting
    * [ABC160 F - Distributing Integers (600点)]( https://atcoder.jp/contests/abc160/tasks/abc160_f )
    * [ARC022 C - ロミオとジュリエット]( https://atcoder.jp/contests/arc022/tasks/arc022_3 )
        * 木の直径を求める問題
        * 全方位木DPより簡単な解法はあるが、全方位木DPの練習になる


## Others
* その他
    * [ABC011 C - 123引き算]( https://atcoder.jp/contests/abc011/tasks/abc011_3 )
    * [ABC017 D - サプリメント]( https://atcoder.jp/contests/abc017/tasks/abc017_4 )
        * しゃくとり法 + DP
    * [ABC037 D - 経路]( https://atcoder.jp/contests/abc037/tasks/abc037_d )
        * メモ化再帰の練習になる
    * [ABC044 C - 高橋君とカード / Tak and Cards (300点)]( https://atcoder.jp/contests/abc044/tasks/arc060_a )
    * [ABC054 D - Mixing Experiment (400点)]( https://atcoder.jp/contests/abc054/tasks/abc054_d )
    * [ABC082 D - FT Robot (500点)]( https://atcoder.jp/contests/abc082/tasks/arc087_b )
    * [ABC104 D - We Love ABC (400点)]( https://atcoder.jp/contests/abc104/tasks/abc104_d )
    * [ABC118 D - Match Matching (400点)]( https://atcoder.jp/contests/abc118/tasks/abc118_d )
    * [ABC122 D - We Like AGC (400点)]( https://atcoder.jp/contests/abc122/tasks/abc122_d )
    * [ABC130 E - Common Subsequence (500点)]( https://atcoder.jp/contests/abc130/tasks/abc130_e )
        * DPを二元累積和で高速化する
    * [ABC132 F - Small Products (600点)]( https://atcoder.jp/contests/abc132/tasks/abc132_f )
    * [ABC135 D - Digits Parade (400点)]( https://atcoder.jp/contests/abc135/tasks/abc135_d )
    * [ABC146 F - Sugoroku (600点)]( https://atcoder.jp/contests/abc146/tasks/abc146_f )
        * dpの更新にRMQが必要
    * [ABC147 E - Balanced Path (500点)]( https://atcoder.jp/contests/abc147/tasks/abc147_e )
        * bitset
    * [ABC157 E - Simple String Queries (500点)]( https://atcoder.jp/contests/abc157/tasks/abc157_e )
        * BitSet + SegmentTree
        * 26個のSegTree( or  BIT)でRSQしてもOK
    * [ABC158 F - Removing Robots (600点)]( https://atcoder.jp/contests/abc158/tasks/abc158_f )
        * ２つDPをやる感じ
        * 最初のどのロボットまで起動するかを求めるところにSegmentTreeが必要
    * [ABC162 F - Select Half (600点)]( https://atcoder.jp/contests/abc162/tasks/abc162_f )
    * [ABC163 E - Active Infants (500点)]( https://atcoder.jp/contests/abc163/tasks/abc163_e )
    * [ARC026 C - 蛍光灯]( https://atcoder.jp/contests/arc026/tasks/arc026_3 )
        * DPの更新にSegmentTree(RMQ)が必要
    * [第２回日経コン D - Shortest Path on a Line (600点)]( https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d )
        * DPの漸化式更新のためにRMQする
