# ACL Beginner Contest
* https://atcoder.jp/contests/abl


## C - Connect Cities (300点)
* keyword
  - UnionFind
* 解法
  - 連結成分を判定するのにUnionFindを使う


## D - Flat Subsequence (400点)
* keywords
  - セグメントツリー、SegmentTree、RMQ(RangeMaxQuery)
* 解法
  - 数列Aを前から見ていきながら次のDPテーブルを更新する
    - `dp[i] = (末尾がiの場合のその時点でのBの長さの最大値)`
    - `dp[i] = max(dp[j] for j in range(i-k, i+k+1))`
    - な感じで更新する（ここでセグツリーを使う）
  - イメージとしてはLISのDPに近い


## E - Replace Digits (500点)
* keywords
  - 遅延セグ木
* 解法



## F - Heights and Pairs (600点)
* keywords
* 解法
