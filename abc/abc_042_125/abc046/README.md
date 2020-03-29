# ABC046
* https://atcoder.jp/contests/abc046


## C - AtCoDeerくんと選挙速報 / AtCoDeer and Election Report (300点)
* 比率を何倍したら、直前の投票数以上になるか考える


## D - AtCoDeerくんと変なじゃんけん / AtCoDeer and Rock-Paper (300点)
* 相手が`P`回パーを出しているとする
* 自分が全てグー出すと`-P`点
* 制約はあるが、とりあえず自分の手のグーをパーに変えてみる
  - 負けてる時(相手がパーの時)、負け(-1点)から引き分け(0点)になるので1点増える
  - 引き分け時(相手がグーの時)、引き分け(0点)から勝ち( 1点)になるので1点増える
* つまりパーは出せば出すほどお得
  - グーパーグーパー...の順にたくさんパーを出しておくのが最適