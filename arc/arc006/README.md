# ARC006
* https://atcoder.jp/contests/arc006


## C - 積み重ね
* keywords
  - 貪欲、LIS
* 解法1 (editorial)
  - 貪欲
* 解法2
  - LIS


## D - アルファベット探し
* keywords
  - 平面図形、同一判定の工夫
* 解法
  - A/B/Cはそれぞれ7x7では12/16/11マスで構成されている
  - 縦横等倍のスケールアップと回転のみが許されているので、A/B/Cを構成するマスとしてあり得る数は以下
    - `A: 12 * k**2 = 3 * x**2`
    - `B: 16 * k**2 = 1 * x**2`
    - `C: 11 * k**2`
  - よって8近傍に関する連結成分を見てマスを数え、上記のどれにあたるかを判定すれば良い
* comments
  - [chokudai今日の一問]( https://twitter.com/chokudai/status/1164839232285712385?s=20 )に選ばれた問題
  - 賢すぎ、思いつかん
  - 適当にdfsを再帰で書くとセグフォる
    - `sys.setrecursionlimit` を設定していても、メモリ制限でセグフォルことがあるらしい
    - List使ってStackとして実装すると通る（面倒かよ）
