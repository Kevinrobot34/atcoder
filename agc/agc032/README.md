# AGC032
* https://atcoder.jp/contests/agc032


## A - Limited Insertion (400点)
まず操作手順が存在するかどうかについて。
操作手順が存在するとすると、必ず`b_i <= i (i = 1,2,...,N)`を満たす。
bがこれを満たすかどうか調べれば良い。

次に操作手順が存在する場合のその構成の仕方について。
手順を逆から考える。`b_i = i`となっているもののうち、iが最大のものが最後に行った手順に対応する。
（落ち着いて考えると正しいことがわかる。）
これを元に手順を最後の方から再構成すれば良い。


## B - Balanced Neighbors (700点)


## C - Three Circuits (800点)
