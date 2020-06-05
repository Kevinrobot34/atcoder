# ARC037
* https://atcoder.jp/contests/arc037


## B - バウムテスト
* keywords
  - DFS、UnionFind、木、連結成分
* 解法1 (editorial)
  - DFS
* 解法2
  - UnionFind


## C - 億マス計算
* 二分探索
* 「K番目の要素がX以下」は「X以下の要素がK個以上」と同値
  - 単調性はまあ自明
  - 判定方法も、bisect_right使えば簡単
    - 一回あたり時間は`O(NlogN)`かかる
      - 頑張れば`O(N)`にもできる
    - 判定する回数は`O(log(MaxA * MaxB))`
* 全体の時間計算量は`O(NlogN * log(MaxA * MaxB))`
