# ABC137
* https://atcoder.jp/contests/abc137


## C - Green Bin (300点)
適当にソートして数える


## D - Summer Vacation (400点)
M日後から0日後(現在)まで順に、どの仕事を受けるべきかを決めていく。
priority_queueを使えばOK


## E - Coins Respawn (500点)
* ベルマンフォード
* まず一回ベルマンフォードをO(V*E)で回す
  - さらにもう一度同じループを回してみて、d[n-1]が変化したかを確認する。
  - もし変化していたら、頂点n-1に到達しうる負のループがあることになる。


## F - Polynomial Construction (600点)
