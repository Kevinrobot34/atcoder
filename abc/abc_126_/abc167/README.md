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
  - Bracket、括弧列
* 解法
* 類題
  - [ARC053 C - 魔法使い高橋君]( https://atcoder.jp/contests/arc053/tasks/arc053_c )
  - [AOJ Volume26-2681 Parentheses]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2681 )
