# ABC138
* https://atcoder.jp/contests/abc138


## C - Alchemist (300点)
ソートして適当に足し算


## D - Ki (400点)
* 木でimos法的なことをする
* DFSの場合
  * Pythonの再帰は遅い。Stack使って書くとぎりぎり通った
  * 再帰で描く場合は `input = sys.stdin.readline` すると良い。だいぶ早くなる。
* BFSの場合
  * queue使うからぎりぎり間に合う。


## E - Strings of Impurity (500点)
* 方針はおよそあってたけど、なんか通せなかった。反省。
* 解法１
  * 前処理として、各アルファベットがi文字目より後に最初に出てくる場所を計算しておく
* 解法２
  * `s2 = s + s` とする
  * s2の各文字について、何番目に現れるかをlistで保持する
  * tの各文字t[i]について次にt[i]が現れるのは何番目かを二分探索で調べる


## F - Coincidence (600点)
