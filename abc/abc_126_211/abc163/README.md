# ABC163
* https://atcoder.jp/contests/abc163


## C -  (300点)



## D - Sum of Large Numbers (400点)
* `i`個選ぶ場合と、`j (!= i)`個選ぶ場合の和は必ず異なる
* 「`i`個選ぶ場合の和は何種類あるか」、が問題
  - 「`0`から`N`までの自然数の中から重複なしで`i`個選ぶ時の和」を考える
    - これの取りうる値は **連続** なのがポイント
    - min: `0 + 1 + ... + (i-1)`
    - max: `(n-i+1) + ... + n`
    - これらの差


## E - Active Infants (500点)
* DP
  - 基本的に活発度が大きい幼児から考えて、両端どちらかに寄せていけばよさそう
  - `d[i][j]=(大きい方からi番目まで見て、左からj番目まで使われている場合の最大値)`
  - O(N^2)


## F - path pass i (600点)
* keywords
  - 木DP、根付き木、DPのインライン化
* 解法1 (editorial)
  - DFSで頑張る
  - 単純パスの総数は `n*(n+1)//2 = comb(n, 2) + n`
  - 求める答えは...
    - 色`k`の頂点を削除したときの連結成分の頂点数を`x`とする
    - 単純パスの総数から `x*(x+1)//2` を引いていったものが答え
  - `n_st[i] = (頂点iの部分木の頂点数)`
  - `cnt[i] = (訪問済み頂点のうち、色iを通過しないとたどり着けない頂点数)`
  - 上記2つをDFSで求めながら答えを計算する
* 解法2
  - mergeテク（Weighted Union Heuristics）を使う
    - maspyさんブログ参照
* References
  - [optさんの解説pdf]( https://twitter.com/opt_coder/status/1252196419424776200?s=20 )
  - [maspyさんの解説]( https://maspypy.com/atcoder-%E5%8F%82%E5%8A%A0%E6%84%9F%E6%83%B3-2020-04-13abc-163 )
