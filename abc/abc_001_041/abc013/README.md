# ABC013
* https://atcoder.jp/contests/abc013


## C - 節制
* 線形計画問題っぽいやつ
* 数式を丁寧に変形していく
  - `O(N)`の全探索でいけることがわかる


## D - 阿弥陀
* keywords
  - 置換、巡回置換、ダブリング
* 解法１
  - あみだくじは置換
    - 巡回置換の組み合わせになっている
    - 巡回置換については、`D`回後のあみだくじの結果がどうなっているかは簡単にわかる
  - 「`i`番目の縦線が`T[i]`番目の縦線に移る」という配列`T`を用意する
    - `1,2,...,N`に対して、あみだくじを下から見てswapしていけば良い
    - `O(M)`
  - `1`から`N`まで走査して、巡回置換を見つけながら答えを計算する
    - `O(N)`
* 解法２
  - 巡回置換であることに気づかなくてもダブリングをすれば`O(M + NlogD)`で解ける
    - editorial
