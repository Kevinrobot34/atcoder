# ABC087
* https://atcoder.jp/contests/abc087


## C - Candies (300点)


##　D - People on a Line (400点)
* l[i]からr[i]へコストd[i]の辺を貼り、有向グラフを作る
* 'No'が答えになるパターンは２通り
  - DAGでないパターン cf.) 入力例4
  - DAGだが数字が合わないパターン cf.) 入力例2
* DAGかどうか知りたいのでとりあえずtopological-sortする
* DAGだったらtopological-sortした上で前から順番に辺を見ていく
  - 初めて訪れた頂点には座標を適当に割り当てる
  - すでに訪れたことある頂点について、新たな情報に矛盾がないかチェックする
