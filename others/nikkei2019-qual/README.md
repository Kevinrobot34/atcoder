# 全国統一プログラミング王
* https://atcoder.jp/contests/nikkei2019-qual


## C - Different Strokes (400点)
* keywords
  - 貪欲法
* 解法
  - `X = (高橋くんの幸福度の総和) - (青木さんの幸福度)`とする
    - 高橋くんは`X`の最大化を目指す
    - 青木さんは`X`の最小化(`-X`の最大化)を目指す
  - 全て青木さんが食べたと仮定すると`X = -sum(bi)`
    - ここから高橋くんと青木さんの選択で`X`がどう変わるかを考える
      - 高橋くんが料理`i`を選ぶと、`X`は`ai+bi`増える
      - 青木さんが料理`j`を選ぶと、`X`は**変化なし**
  - 以上の考察から、
    - 高橋くんは`ai+bi`が大きいものから食べるのが良い
    - 青木さんは次高橋くんが大きな`ai+bi`を選べないように`ai+bi`が最大のものを食べるのが良い
  - よって、`ai+bi`でソートして、`0,2,4,...`番目を高橋くんが食べることになる


## D - Restore the Tree (500点)
* keywords
  - グラフ、トポロジカルソート
* 解法
  - トポロジカルソートして、前から順番に答えの配列を更新すれば良いだけ


## E - Weights on Vertices and Edges (800点)
* keywords
  - グラフ、UnionFind
* 解法
  - editorialの通り
  - https://sigma1113.hatenablog.com/entry/2019/01/28/225900
