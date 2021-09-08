# ABC172
* https://atcoder.jp/contests/abc172


## C - Tsundoku (300点)
* keywords
  - 累積和、二分探索、しゃくとり法
* 解法1
  - `A`と`B`の累積和を取る(`A_cs`、`B_cs`)
  - `A_cs[i] + B_cs[j] <= K`なる`(i, j)`を探す
    - `i`を固定すれば、`j`は二分探索で求まる
* 解法2
  - `A`と`B`の累積和を取る(`A_cs`、`B_cs`)
  - `A_cs[i] + B_cs[j] <= K`なる`(i, j)`を探す
    - しゃくとり法
    - `i`を`0, 1, 2, ..., n`と動かすと、`j`は単調に減少する
* comment
  - C問題にしては難しい


## D - Sum of Divisors (400点)
* keywords
  - エラトステネスの篩、調和級数
* 解法1
  - エラトステネスの篩的な発想で `O(NlogN)`
* 解法2 (editorial)
  - まずナイーブな `O(N^2)` のコードを書いてみる
    ```
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            if i % j == 0:
                ans += i
    ```
    - このコードの内側のfor文は `for j in range(1, n + 1)` でも結果は同じ
  - 上記を踏まえると2つのfor文を入れ替えても良い
    ```
    ans = 0
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            if i % j == 0:
                ans += i
    ```
  - ここまで来ると内側のfor文は `ans += (n//j) * (n//j + 1) // 2` と置き換えられることがわかる
  - `O(N)`
* comments
  - editorialの方法賢い


## E - NEQ (500点)
* keywords
  - 完全順列、Combination、Permutation、包除原理
* 解法
  - そもそも、全ての要素が相異なるような数列自体は `perm(m, n)`通り存在する
  - 数列`A`を`1,2,3,...,n`で固定する
    - この`A`と数列`B`のすべての要素が相異なるような場合を数える
    - 完全順列の拡張的なイメージ
    - 包除原理的な数え方をする
      - `A`と`B`で一致している要素の数を`i`個とする
        - このような順列の数は `comb(n, i) * perm(m-i, n-i)`通り
      - よって `( \sum_{i=0}^{n} (-1)**i * comb(n, i) * perm(m-i, n-i) ) * perm(m, n)`
  - `O(M + N)`


## F - Unfair Nim (600点)
* keywords
  - Nimゲーム、Xor
