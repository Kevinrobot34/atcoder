# ABC083
* https://atcoder.jp/contests/abc083


## C - Multiple Gift (300点)
* xを「yを超えない範囲で何度2倍できるか」を数える


##　D - Wide Flip (500点)
* flipできる区間が短い分には問題ない
  - `K=1`とすれば必ず全てを`0`にできる
* そもそも全てを`0`にするにはどうすればいいか
  - `0`と`1`の境界を一つずつ無くしていく
    - `s01t`という文字列があった場合
      - 0から左側(`s0`) **全て** を反転する
      - 1から右側(`1t`) **全て** を反転する
    - のどちらかを行えばこの`01`の境界をなくせる
    - （反転こそされるが、他の境界の数の増減はないのがポイント）
      - 全てでなく中途半端に反転すると境界が増えたりしうる
* 今回、選択する区間の長さをできるだけ長く取りたいので、
  - 各境界に対し、長い方の区間を反転することにしておくのが最適
  - 左から`k`文字目と`k+1`文字目が異なるとすると、
    - 左側の区間は長さ`k`、右側の区間は長さ`n-k`
    - よって`max(k, n-k)`の反転をして、境界を無くせる
* 今回、一旦`K`を固定すると長さ`K`以上の連続する区間を自由にflipできる
  - よって答えは`min{max(k, n-k) | kとk+1で文字が異なる}`
