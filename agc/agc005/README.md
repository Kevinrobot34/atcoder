# AGC005
* https://atcoder.jp/contests/abc140


## B - Minimum Sum (400点)
* 直接計算は厳しい
* `min(a[l], ..., a[r])`の値が`x`となるような区間`[l, r]`を考える。
  - その数を`c[x]`とすると、答えは`c[x] * x`を足し合わせたもの
* `c[x]`の求め方を考える
  - 小さい方から求めていく
  - xのidxを保持
  - xより小さく、左側で一番近いものの場所をidx_lとする
  - xより小さく、右側で一番近いものの場所をidx_rとする
  - `c[x] = (idx - idx_l) * (idx_r - idx)`
  - BITを使ってindexを管理すれば、`idx_l`と`idx_r`の取得が`O(logN)`で出来る


## C - Tree Restoring (700点)
