# ABC167
* https://atcoder.jp/contests/abc167


## C - Skill Up (300点)
* keyword
  - bit全探索
* 解法
  - 「どの参考書を読むか」についてbit全探索する
  - `O((N+M) 2^N)`
  - [提出]( https://atcoder.jp/contests/abc167/submissions/13037735 )


## D - Teleporter (400点)
* keyword
  - loop, ダブリング
* 解法1
  - 同じ町に再度訪れるまでまずシミュレーションする
  - あとはよしなに余りを計算したりするだけ
  - `O(N)`
  - [提出]( https://atcoder.jp/contests/abc167/submissions/13047261 )
* 解法2
  - ダブリング
  - `O(NlogK)`
  - [提出]( https://atcoder.jp/contests/abc167/submissions/13099779 )
* 類題
  - [ABC030 D - へんてこ辞書]( https://atcoder.jp/contests/abc030/tasks/abc030_d )


## E - Colorful Blocks (500点)
* keyword
  - combination
* 解法
  - 計算量的にきついがまずDPを考えてみる
    - `dp[i][j] = (左からi個のブロックに色を塗り、隣接するj組のブロックが同じ色であるような場合の数)`
      - 初期値
        - `dp[1][0] = M`
        - `dp[1][j] = 0 (j>0)`
      - 漸化式
        - `dp[i+1][j] = dp[i][j-1] + dp[i][j] * (M-1)`
    - これを手で計算してみると
      - `dp[i+1][j] = comb(i, j) * M * (M-1)**(i-j)`
      - と分かる
    - [提出]( https://atcoder.jp/contests/abc167/submissions/13059530 )


## F - Bracket Sequencing (600点)
* keyword
  - Bracket、括弧列、貪欲法
* 解法１
  - [参考]( https://kmjp.hatenablog.jp/entry/2020/05/10/0930 )
  - 括弧列を扱う際の定石
    - 変数`v`を用意し、0にしておく
    - 与えられた文字列を前から見て、`(`なら`v+=1`、`)`なら`v-=1`をしていく
    - 上記の処理をしていく過程で常に`v>=0`であり、最終的に`v=0`となればその文字列は括弧列
    - `v`はそこまで見た際の余分な`(`の数と考えることができる
  - `s[i]`に対し上記の処理を行った際の最終的な`v`の値を`f`、途中の`v`の値の最小値を`m`とする
    - `(f, m)`のとりうる値の範囲は以下の３種類
      - `f>=0`, `m=0` : `((()`など
      - `f>=0`, `m<0` : `)((` など
      - `f< 0`, `m<0` : `()))` など
    - 値が`v(>=0)`となっている文字列に、`(f, m)`な文字列を連結することを考える
      - `v+m>=0`なら正しく結合でき、`v->v+f`となる
    - 初期値`v=0`から、どのような順番で`(f, m)`を適用すれば`v>=0`を保ち、最終的に`v=0`にできるかを考えれば良い
  - `f>=0 : '('が余ってる`と`f<0 : ')'が余ってる`に分けて考える
  - `f>=0`なものだけに注目すると、`m`が大きい順に貪欲に適用しておけば最適であることがわかる
    - どのような順番で連結しても`v`は増えていく
    - `v+m>=0`を満たせるかどうかが問題
      - ある`(fi, mi)`について、`mi`よりも`m`が大きいものは先に連結しておくべき
    - こうして求めた`v`は、いくつ`(`が余っているかに対応する [A]
  - `f<0`について [x]
    - 文字列の`(`と`)`を反転し、後ろから読んで見ることにする
      - `()))`は`((()`と考える的な
    - `(f, m)`は`(-f, m-f)`になる
    - これらに対して、`f>=0`の操作を行う
      - こうして求めた`v`がいくつ`)`が余っているかに対応する [B]
  - [A]と[B]が同じ値であれば、整合性の取れた括弧列になっている
  - [提出]( https://atcoder.jp/contests/abc167/submissions/13135017 )
* 解法２
  - [参考]( https://merom686.hatenablog.com/entry/2020/05/10/231411 )
  - 解法１と [x] までは同じ
  - `f<0`について
    - `f-m(>=0)`の大きい順に連結するのが最適
      - ある`v`に対し、`(f, m)`を連結する際に、`v+m>=0`であればよく、`v->v+f`となるのであった
        - 適用後から見ると、`v+m`は`v+f`より`f-m`小さい値になる
        - 連結していくたびに`v`は単調に減少するので、最後の方は`f-m`が小さい方が良いことになる
        - つまり、`f-m`が大きい順にやるべき
          ```
          v ---
                \
                  --- v+f
                   ↑
                  f-m
                   ↓
            --------- v+m
          ```
  - [提出]( https://atcoder.jp/contests/abc167/submissions/13135296 )
* 類題
  - [ARC053 C - 魔法使い高橋君]( https://atcoder.jp/contests/arc053/tasks/arc053_c )
  - [AOJ Volume26-2681 Parentheses]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2681 )
