# ABC018
* https://atcoder.jp/contests/abc018


## C - 菱型カウント
* 縦方向と横方向は独立に考えられるのがポイント


## D - バレンタインデー
* 半分全列挙
  - 女子側固定する(`2^N`)
  - どの男子を入れるべきかは貪欲に決まる(`O(NM + MlogM)`)
  - `O(NM2^N)`
  - サイズ`k`のbit部分列の生成はアリ本に載っているので要確認
