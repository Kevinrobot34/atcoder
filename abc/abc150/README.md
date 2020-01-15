# ABC150
* https://atcoder.jp/contests/abc150


## C - Count Order (300点)
* `N!`通りの順列の全探索
  - python : `itertools.permutations(range(1, n+1))`
  - C++ : `next_permutation`


## D - Semi Common Multiple (400点)
* ちょっとした数学の問題


## E - Change a Little Bit (500点)
* 難しい数え上げ


## F - Xor Shift (600点)
* `k`を固定すると、`x`は`x = a[k] ^ b[0]`しかあり得ないことが分かる。
* あとは任意の`k`に対して、数列`a'`と`b`が一致するかを調べれば良い。
  - ナイーブに考えると`a'`は`x`に依存するので、一致するかどうか調べるのに毎回`a'`を計算しないといけない
    - 一致の判定に`O(N)`かかってしまう
  - 階差数列的な考え方をして、数列`a'`と`b`が一致するか比較する代わりに、隣接する項のXorをとった数列を比較すればよい
    - Xor階差数列的なものは、`x`に依存しない
    - RollingHash、KMP、Z-Algorithmなどで前処理`O(N)`、判定`O(1)`で可能
* 参考
  - http://drken1215.hatenablog.com/entry/2020/01/12/115800
  - https://atcoder.jp/contests/abc150/submissions/9407665
