# ARC011
* https://atcoder.jp/contests/arc011


## A - 鉛筆リサイクルの新技術
* keywords
  - シミュレーション、計算量見積もり
* 解法
  - シミュレーションするだけ
  - `O(N)`
    - `x[i] = (i回目に手元にある鉛筆の本数)`
      - `x[0]`
      - `x[i] = (x[i-1] // m) * n + (x[i-1] % m)`
      - `x[i] < x[i-1]`
        - `x[i] = a[i]*m + b[i]`の形で表すと示せる
          - `x[i] = a[i-1] * n + b[i-1] < a[i-1] * m + b[i-1] = x[i-1]`
        - 毎回1本は減るので、高々`O(N)`


## B - ルイス・キャロルの記憶術
* keyword
  - str.translate
* 解法
  - 適当に文字を置換するだけ
  - `I`みたいな子音のみの単語はスキップする


## C - ダブレット
* keywords
  - 最短経路(Dijkstra/01-BFS/etc)、経路復元
* comments
  - 辺の数は高々`N*30`なのでDijkstraで十分間に合う
