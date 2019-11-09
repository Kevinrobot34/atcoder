# Segment Tree
`N`個からなる列に対して

* 連続する区間に(モノイドをなす)演算をする
* 一点の値を更新する

の両方を`O(logN)`で行えるデータ構造。
構築にかかる時間は`O(N)`。

## example
### RMQ - Range Minimum Query
* https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A

### RSQ - Rannge Sum Query
* https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B

## Monoid
### definition
集合`S`、その上の二項演算`op(x, y)`が与えられた時、
以下の条件を満たすならば`(S, op)`を**モノイド**という。
* 結合律
  - `S`の任意の元`a, b, c`に対して、`op(op(a, b), c) = op(a, op(b, c))`
* 単位元の存在
  - `S`のある元`e`が、`S`の任意の現`a`に対して、`op(a, e) = op(e, a) = a`を満たす

結合律の満たすものは**半群**という。
モノイドは「単位元を持つ半群」ということになる。

具体例
* (N, +) : 半群だが、単位元が存在せずモノイドではない
* (Z, +) : 0を単位元とするモノイド
* (R, \*) : 1を単位元とするモノイド

`int`をint型で扱える整数とすると、
* (`int`, +) : 0を単位元とするモノイド
* (`int`, min) : `INT_MAX`を単位元とするモノイド


## Reference
* https://www.slideshare.net/iwiwi/ss-3578491
  - 秋葉さんによるデータ構造の解説
* http://beet-aizu.hatenablog.com/entry/2017/09/10/132258
* https://www.creativ.xyz/segment-tree-abstraction-979/
  - セグツリーの抽象化について
* https://ei1333.github.io/luzhiled/snippets/structure/segment-tree.html
  - セグツリーの抽象化と遅延評価について
* http://koba-e964.hatenablog.com/entry/2016/12/14/214132
